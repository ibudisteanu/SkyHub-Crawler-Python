from Crawler.CrawlerBasic import CrawlerBasic

from Crawler.Helpers.LinksHelper import LinksHelper
from Crawler.Helpers.LinksDB import LinksDB

from Crawler.Objects.ObjectLink import ObjectLink
from Server.ServerAPI import ServerAPI

class CrawlerProcess(CrawlerBasic):

    cssBreadcrumbsChildrenList = ''
    cssBreadcrumbsChildrenListElementHref = ''
    cssBreadcrumbsChildrenListElement = ''

    #Process Data and Create new Objects
    def processScrapedData(self, url):

        self.title = self.cleanText(self.title)
        self.fullDescription = self.cleanText(self.fullDescription)
        self.shortDescription = self.cleanText(self.shortDescription)
        self.author = self.cleanText(self.author)

        self.parentId = self.createParents()

        # validate
        validation = self.validate()

        if validation != '':
            if LinksDB.findLinkObjectAlready(url) is None:

                if validation in ['news', 'topic']:

                    topicObject = LinksDB.findLinkObjectAlready(self.currentPageURL, self.title or self.ogTitle, True)

                    if topicObject is None:  #we have to add the topic

                        title = self.title or self.ogTitle
                        description = self.fullDescription or self.ogDescription or self.shortDescription

                        if len(title) > 5 and len(description) > 30:
                            topicId = ServerAPI.postAddTopic(self.url, self.user, self.parentId,
                                                             title,
                                                             description,
                                                             self.ogDescription or self.shortDescription,
                                                             self.keywords, self.images, self.date,
                                                             self.websiteCountry or self.language, self.websiteCity, self.websiteLanguage or self.language, -666, -666,
                                                             self.author, self.authorAvatar)

                            topicObject = ObjectLink(self.currentPageURL, 'topic', topicId, self.title, self.parentId)
                            LinksDB.addLinkObject(topicObject)

                    if topicObject is not None:

                        topicId = topicObject.id
                        print("new topic ", topicId)

                        if len(self.replies) > 0:
                            for reply in self.replies:
                                replyObjectURL = self.currentPageURL+reply['title'] + reply['description']
                                replyObjectTitle = reply['title'] + reply['description']

                                replyObject = LinksDB.findLinkObjectAlready(replyObjectURL, replyObjectTitle, True)

                                if replyObject is None: # we have to add the reply

                                    if len(reply['description']) > 40:
                                        replyId = ServerAPI.postAddReply(self.url, self.user, topicId,
                                                                         "", reply['title'], reply['description'],
                                                                         '', [], reply['date'],
                                                                         self.websiteCountry or self.language, self.websiteCity, self.websiteLanguage or self.language, -666, -666,
                                                                         reply['author'], reply['authorAvatar'])

                                        replyObject = ObjectLink(replyObjectURL, 'reply', replyId, replyObjectTitle, topicId)
                                        LinksDB.addLinkObject(replyObject)

                                if replyObject is not None:
                                    replyId = replyObject.id
                                    print("new reply ", replyId)

                    pass
                elif self.validate() in ['category', 'forum']:
                    pass
                else:
                    pass
            else:
                print("Already processed ", url)

        return None

    def processScrapedData(self, url):

        self.parents = []

        if len(self.title) > 0:
            for i in reversed(range(1, 100)):
                parent = response.css(self.cssBreadcrumbsChildrenList+':nth-child('+str(i)+')')
                parentText = self.extractFirstElement(parent.css(self.cssBreadcrumbsChildrenListElement+'::text'))
                parentURL = self.extractFirstElement(parent.css(self.cssBreadcrumbsChildrenListElementHref+'::attr(href)'))

                if parentText != '':
                    self.parents.append({'name':parentText, 'url':parentURL, 'index': i})


        self.parents = list(reversed(self.parents)) #changing the order

    # ---------------------
    # ---------------------
    # ---------------------- GRAND PARENTS
    # ---------------------
    # ---------------------
    def createParents(self):

        grandparentId = self.forumGrandParentId

        # if len(self.parents) == 0:
        #     self.parents.append({'name': '', 'url': self.url})

        if len(self.parents) > 0:
            ok = False
            for parent in self.parents:
                if parent['name'] == '':
                    ok = True

            if ok == False:
                self.parents = [{'name': '', 'url': self.url}] + self.parents

        for parent in self.parents:

            parentName = self.websiteName+' '+parent['name']
            parentObject = LinksDB.findLinkObjectAlready(parent['url'], parentName)

            if parentObject is None:

                image = self.websiteImage or self.ogImage
                if (image == '') and (len(self.images) > 0): image = self.images[0]

                forumId = ServerAPI.postAddForum(self.url, self.user, grandparentId, self.websiteName +" "+ parent['name'],
                                                 self.websiteName + " " + parent['name'], self.websiteName +" "+ parent['name'],
                                                 image,
                                                 self.websiteCover,
                                                 self.keywords,
                                                 self.date, self.websiteCountry or self.language, self.websiteCity, self.websiteLanguage or self.language, -666, -666)

                parentObject = ObjectLink(parent['url'], 'forum', forumId, parentName, grandparentId)
                LinksDB.addLinkObject(parentObject)

            grandparentId = parentObject.id
            #print("grandparentId   ",grandparentId)

        return grandparentId
