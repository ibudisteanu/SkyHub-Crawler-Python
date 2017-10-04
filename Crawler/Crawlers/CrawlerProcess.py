from Crawler.Helpers.LinksDB import LinksDB
from Crawler.Objects.ObjectLink import ObjectLink
from Crawler.SmartCrawlers.CrawlerBasic import CrawlerBasic
from Server.ServerAPI import ServerAPI


class CrawlerProcess(CrawlerBasic):

    cssBreadcrumbsChildrenList = ''
    cssBreadcrumbsChildrenListElementHref = ''
    cssBreadcrumbsChildrenListElement = ''

    #variables

    author = ''
    authorLink = ''
    authorAvatar = ''

    parents = []
    parentId = ''

    # Process Data and Create new Objects
    def processScrapedData(self, url):

        self.title = self.cleanText(self.title)
        self.fullDescription = self.cleanText(self.fullDescription)
        self.shortDescription = self.cleanText(self.shortDescription)
        self.author = self.cleanText(self.author)

        self.parentId = self.createParents()

        return None

    def crawlerProcess(self, response, url):

        super().crawlerProcess(response, url)

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
            parentObject = LinksDB.findLinkObjectAlready(self.domain, parent['url'], title=parentName, description='')

            print("@@@@@@@@@@@@@", parentObject)

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
                LinksDB.addLinkObject(self.domain, parentObject)

            if parentObject is not None:
                grandparentId = parentObject.id
                #print("grandparentId   ",grandparentId)

        return grandparentId

    def toString(self):

        super().toString()

        if len(self.parents) > 0: print("parents", self.parents)

        if isinstance(self.author, str):
            if len(self.author) > 0: print("author:", self.author, self.authorLink)
            if len(self.authorAvatar) > 0: print("authorAvatar", self.authorAvatar)
        else:
            print("Author")
            self.author.toString()
