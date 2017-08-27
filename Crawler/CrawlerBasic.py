from urllib.parse import urlparse

import scrapy
from Crawler.Helpers.LinksHelper import LinksHelper

from Crawler.Helpers.AttrDict import AttrDict


class CrawlerBasic(scrapy.Spider):

    title = ''
    shortDescription = ''
    fullDescription = ''
    images = []
    keywords = []
    author = ''
    authorLink = ''
    language = ''
    date = ''
    currentPageURL=''

    ogTitle = ''
    ogDescription = ''
    ogImage = ''
    ogSiteName = ''
    ogType = ''

    url = ''

    def __init__(self):
        pass

    def extractFirstElement(self, list, returnValue='', index=0):
        if len(list) > index: return list[index].extract()
        return returnValue


    def basicProcess(self, response):
        self.title = self.extractFirstElement(response.xpath('//title/text()'))
        self.keywords = self.extractFirstElement(response.xpath("//meta[@name='keywords']/@content"))
        self.shortDescription = self.extractFirstElement(response.xpath("//meta[@name='description']/@content"))

        self.language = self.extractFirstElement(response.xpath("//meta[@name='language']/@content")) #format: "Romanian"
        self.language = self.extractFirstElement(response.xpath("//meta[@http-equiv='content-language']/@content")) #format: "ro"

        self.ogTitle = self.extractFirstElement(response.xpath('//meta[@property="og:title"]/@content'))
        self.ogDescription = self.extractFirstElement(response.xpath('//meta[@property="og:description"]/@content'))
        self.ogImage = self.extractFirstElement(response.xpath('//meta[@property="og:image"]/@content'))
        self.ogSiteName = self.extractFirstElement(response.xpath('//meta[@property="og:site_name"]/@content'))
        self.ogType = self.extractFirstElement(response.xpath('//meta[@property="og:type"]/@content'))

        self.currentPageURL = response.url

        if self.ogTitle != '': self.title = self.ogTitle
        if self.ogDescription != '': self.shortDescription = self.ogDescription
        if self.ogImage != '':
            self.images = AttrDict(img=self.ogImage, title=self.title, description=self.shortDescription)


    def crawlerProcess(self, response):
        pass

    def start_requests(self):
        for url in self.start_urls:
            print("processing url",url)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        LinksHelper.addLinkVisited(response.url)

        self.basicProcess(response)
        self.crawlerProcess(response)

        self.title = self.cleanText(self.title)
        self.fullDescription = self.cleanText(self.fullDescription)
        self.shortDescription = self.cleanText(self.shortDescription)
        self.author = self.cleanText(self.author)

        self.toString()

        if self.validate() != '':
            if LinksHelper.checkLinkProcessedAlready(response.url) == False:
                if self.validate() == 'news':
                    pass
                elif self.validate() == 'category':
                    pass
                else:
                    pass
            else:
                print("Already processed ", response.url)

        for next_page in response.css('a'):

            next_page = self.extractFirstElement(next_page.xpath('@href'))

            sharpIndex = next_page.find('#')
            if sharpIndex >= 0:
                next_page = next_page[0: sharpIndex]

            parsed_url = urlparse(next_page)

            if bool(parsed_url.scheme) == False:
                newUrl = self.url
                if newUrl[:-1] == '/': newUrl = newUrl + '/'
                next_page = newUrl + next_page

            #print(next_page)

            try:

                yield scrapy.Request(url = next_page, callback=self.parse)

            except ValueError:
                pass



    def getNextPages(self, response):
        pass


    def validate(self):
        return ''

    def toString(self):
        print("title:", self.title)
        print("shortDescription:", self.shortDescription)
        print("fullDescription:", self.fullDescription)
        print("language:", self.language)
        print("images:", self.images)
        print("keywords:", self.keywords)
        print("author:", self.author, self.authorLink)
        print("date:", self.date)


        # print("og:title", self.ogTitle)
        # print("og:description", self.ogDescription)
        # print("og:image", self.ogImage)
        # print("og:site_name", self.ogSiteName)
        # print("page_url", self.currentPageURL)

        print("url:", self.currentPageURL)
        print("validate", self.validate())

    def cleanText(self, text):

        return text

        #
        # cleaner = Cleaner()
        # cleaner.javascript = True  # This is True because we want to activate the javascript filter
        # #cleaner.style = True  # This is True because we want to activate the styles & stylesheet filter
        # cleaner.remove_tags = ['script','div']
        # return cleaner.clean_html(text)