import dateparser

from Crawler.Helpers.LinksDB import LinksDB
from Crawler.Helpers.JSONDB import JSONDB
from Crawler.Objects.ObjectLink import ObjectLink
from Crawler.SmartCrawlers.CrawlerBasic import CrawlerBasic
from Server.ServerAPI import ServerAPI

class CrawlerProcess(CrawlerBasic):
    cssBreadcrumbsChildrenList = ''
    cssBreadcrumbsChildrenListElementHref = ''
    cssBreadcrumbsChildrenListElement = ''
    cssTitle = ""
    cssAuthor = ""
    cssAuthorLink = ""
    cssFullDescription = ""
    cssDateText = ""
    cssDate = ""
    cssParent = ''

    author = ''
    authorLink = ''
    authorAvatar = ''
    parents = []
    parentId = ''
    removeShortDescription = False
    saveJSONFile = False

    # Process Data and Create new Objects
    def processScrapedData(self, url):
        self.title = self.cleanText(self.title)
        self.fullDescription = self.cleanText(self.fullDescription)
        self.shortDescription = self.cleanText(self.shortDescription)
        self.author = self.cleanText(self.author)

        if self.saveJSONFile and self.validate():
            JSONDB.addJSONObject(self.domain, self.toJSON())

        return None


    def crawlerProcess(self, response, url):

        def FormatDate(date, date_parser):
            for k, v in date_parser.items():
                date = date.replace(k, v)
            return date

        super().crawlerProcess(response, url)
        self.parents = []

        if self.removeShortDescription:
            self.shortDescription = ''
            self.ogDescription = ''

        if self.cssFullDescription:
            self.fullDescription = ''.join(response.css(self.cssFullDescription).extract()).strip()

        for srcItem, destItem in zip([self.cssAuthor, self.cssAuthorLink, self.cssTitle], [self.author, self.authorLink, self.title]):
            if srcItem:
                destItem = self.extractFirstElement(response.css(srcItem))

        if len(self.cssParent):
            self.parents = []

            parent = response.css(self.cssParent)
            parentText = self.extractFirstElement(parent.css('::text'))
            parentURL = ' '.join((parent.css('::attr(href)').extract()))

            if parentText and parentURL:
                self.parents.append({'name': parentText, 'url': parentURL, 'index': 1})

        if self.cssDateText:  # Text format like 22 Jul 2017
            date = self.extractText(response.css(self.cssDateText)).lower()
            date = FormatDate(date, {'noiembrie':'nov', 'ianuarie':'jan', 'mai':'may', 'martie':'mar', 'iunie':'jun', 'septembrie':'sep', 'iulie':'jul', 'februarie':'feb'})
            date = FormatDate(date, {'luni':'monday', 'marti':'tuesday', 'marţi':'tuesday', 'miercuri':'thursday', 'joi':'wednesday', 'vineri':'friday', 'sambata':'saturday', 'sambătă':'saturday', 'sâmbătă':'saturday', 'duminica':'sunday', 'duminică':'sunday'})
            date = '%s ' % date.replace(',', ' ')

            print('Result date #1', date)
            try:
                self.date = dateparser.parse(date)
            except ValueError:
                print("Error dataparser.parse(", date, " )");

            print('Result date #2', self.date)
        else:  
            # Get timestamp format if cssDateText is a empty string.
            if self.cssDate:
                self.date = self.extractText(response.css(self.cssDate))

        if len(self.title) and len(self.cssBreadcrumbsChildrenList):
            self.parents = []

            for i in reversed(range(1, 100)):
                parent = response.css(self.cssBreadcrumbsChildrenList + ':nth-child(%s)' % i)
                parentText = self.extractFirstElement(parent.css(self.cssBreadcrumbsChildrenListElement + '::text'))
                parentURL = self.extractFirstElement(parent.css(self.cssBreadcrumbsChildrenListElementHref + '::attr(href)'))

                if parentText:
                    self.parents.append({'name':parentText, 'url': parentURL, 'index': i})

            self.parents = list(reversed(self.parents)) # Changing the order

    ### GRAND PARENTS ###
    def createParents(self):
        grandparentId = self.forumGrandParentId

        if not len(self.parents):
            self.parents.append({'name': '', 'url': self.url})

        if len(self.parents):
            bOk = False
            for parent in self.parents:
                if parent['name'] == '':
                    bOk = True

            if not bOk:
                self.parents = [{'name': '', 'url': self.url}] + self.parents

        print("PARENTS ###########", self.parents)

        for parent in self.parents:
            parentName = self.websiteName+' '+parent['name']
            parentObject = LinksDB.findLinkObjectAlready(self.domain, parent['url'], title=parentName, description='')

            print("@@@@@@@@@@@@@", parentName, parentObject)

            if parentObject is None:
                image = self.websiteImage or self.ogImage
                if not image and len(self.images):
                    image = self.images[0]

                forumId = ServerAPI.postAddForum(self.url, '', self.user, grandparentId, self.websiteName + " " + parent['name'],
                                                 self.websiteName + " " + parent['name'], self.websiteName + " " + parent['name'],
                                                 image,
                                                 self.websiteCover,
                                                 self.keywords,
                                                 self.date, self.websiteCountry or self.language, self.websiteCity, self.websiteLanguage or self.language, -666, -666)

                parentObject = ObjectLink(parent['url'], 'forum', forumId, parentName, grandparentId)
                LinksDB.addLinkObject(self.domain, parentObject)

            if parentObject:
                grandparentId = parentObject.id

        return grandparentId

    def toString(self):
        super().toString()

        if len(self.parents):
            print("parents", self.parents)

        if isinstance(self.author, str):
            if self.author:
                print("author:", self.author, self.authorLink)
            if self.authorAvatar:
                print("authorAvatar", self.authorAvatar)
        else:
            print("Author")
            self.author.toString()

    def toJSON(self):
        json = super().toJSON()

        if not isinstance(self.author, str):
            json.author = self.author.toJSON()
        else:
            for item in ('author', 'authorLink', 'authorAvatar'):
                if item:
                    json[item] = eval('self.{}'.format(item))
        return json
