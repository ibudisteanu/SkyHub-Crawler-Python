from urllib.parse import urlparse

import time

import requests
import scrapy
from parsel import Selector

from Crawler.Helpers.AttrDict import AttrDict
from Crawler.Helpers.LinksHelper import LinksHelper
from Crawler.Helpers.LinksDB import LinksDB

class CrawlerBasic(scrapy.Spider):
    url = ''
    domain = ''
    testingURL = ""

    websiteName = ''
    websiteImage = ''
    websiteCover = ''
    websiteCountry = ''
    websiteCity = ''
    websiteLanguage = ''
    user = 'muflonel2000'

    forumGrandParentId = ''

    linksQueue = []
    linksQueueIndex = 0

    ONLY_ONE_PAGE = False
    MAXIMUM_NUMBER_PAGES = 0
    INFINITE_LOOP = False

    rejectionSubstr = []

    title = ''
    shortDescription = ''
    fullDescription = ''
    images = []
    keywords = []

    language = ''
    date = None
    currentPageURL=''

    ogTitle = ''
    ogSite = ''
    ogDescription = ''
    ogImage = ''
    ogSiteName = ''
    ogType = ''

    lastUpdate = ''

    def __init__(self,  user='', url='', forumGrandParentId = '', websiteName='', websiteImage='', websiteCover = '',  websiteCountry = '', websiteCity = '', websiteLanguage = ''):

        if user != '': self.user = user
        if forumGrandParentId != '': self.forumGrandParentId = forumGrandParentId
        if websiteName != '': self.websiteName = websiteName
        if websiteCover != '': self.websiteCover = websiteCover
        if websiteImage != '': self.websiteImage = websiteImage
        if websiteCountry != '': self.websiteCountry = websiteCountry
        if websiteCity != '': self.websiteCity = websiteCity
        if websiteLanguage != '': self.websiteLanguage = websiteLanguage

        self.restarts = 0

        if url != '': self.url = url

        self.session = requests.Session()

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):

        spider = super(CrawlerBasic, cls).from_crawler(crawler, *args, **kwargs)
        spider.MAXIMUM_NUMBER_PAGES = cls.MAXIMUM_NUMBER_PAGES
        spider.INFINITE_LOOP = cls.INFINITE_LOOP
        spider.linksQueueIndex = 0
        spider.linksQueue = []

        print("spider.MAXIMUM_NUMBER_PAGES", spider.MAXIMUM_NUMBER_PAGES);

        crawler.signals.connect(spider.idle, signal=scrapy.signals.spider_idle)
        return spider

    # tutorial based on https://stackoverflow.com/questions/37291412/call-parse-method-in-spider-closed-method/37318392#37318392
    def idle(self):

        if self.INFINITE_LOOP == False: return False

        print("Spider is restarting - max pages", self.MAXIMUM_NUMBER_PAGES, self.linksQueueIndex)
        if self.linksQueueIndex != 0 and self.linksQueueIndex >= len(self.linksQueue):
            self.restarts += 1
            self.linksQueueIndex = 0
            self.linksQueue = []
            scrapy.linksQueueIndex = 0
            scrapy.linksQueue = []
            self.crawler.engine.crawl( scrapy.Request(self.start_urls[0],dont_filter=True), self)

    def extractFirstElement(self, list, returnValue='', index=0):
        if len(list) > index: return list[index].extract()
        return returnValue

    def extractText(self, list, returnValue='', index=-1):

        if index == -1:
            if len(list) > 0:
                s = ' '.join(list.extract())
                if s is not None: return s.strip()

            return returnValue

        if (index > 0) and (len(list) > index): return list[index].extract()
        return returnValue


    def crawlerProcess(self, response, url):

        try:
            self.title = self.extractFirstElement(response.xpath('//title/text()'))
            self.keywords = self.extractFirstElement(response.xpath("//meta[@name='keywords']/@content"))
            self.shortDescription = self.extractFirstElement(response.xpath("//meta[@name='description']/@content"))

            self.language = self.extractFirstElement(response.xpath("//meta[@name='language']/@content"), self.language) #format: "Romanian"
            self.language = self.extractFirstElement(response.xpath("//meta[@http-equiv='content-language']/@content"), self.language) #format: "ro"
            self.language = self.extractFirstElement(response.css("html::attr(lang)"), self.language) #format: "ro"
            self.language = self.extractFirstElement(response.xpath("//meta[@name='description']/@ro"), self.language) #format: "ro"

            self.ogTitle = self.extractFirstElement(response.xpath('//meta[@property="og:title"]/@content'))
            self.ogSiteName = self.extractFirstElement(response.xpath('//meta[@property="og:site_name"]/@content'))
            self.ogDescription = self.extractFirstElement(response.xpath('//meta[@property="og:description"]/@content'))
            self.ogImage = self.extractFirstElement(response.xpath('//meta[@property="og:image"]/@content'))
            self.ogSiteName = self.extractFirstElement(response.xpath('//meta[@property="og:site_name"]/@content'))
            self.ogType = self.extractFirstElement(response.xpath('//meta[@property="og:type"]/@content'))

            self.currentPageURL = url

            if self.ogTitle != '': self.title = self.ogTitle
            if self.ogDescription != '': self.shortDescription = self.ogDescription
            if self.ogImage != '':
                self.images = [AttrDict(type='file', typeFile='image', url=self.ogImage, img=self.ogImage, title=self.title, description=self.shortDescription)]

            if self.websiteName == '' and self.ogSiteName != '': self.websiteName = self.ogSiteName

            print("keywords_META", self.keywords)

            self.lastUpdate = time.time()

            #if url == self.url:

            if self.websiteName == '': self.websiteName = self.title or self.ogTitle
            if self.websiteImage == '': self.websiteImage = self.ogImage
            if self.websiteCountry == '': self.websiteCountry = self.language


        except ValueError:

            print("ERRRO!!!! processing url")
            self.title = ""
            self.ogTitle = ""
            pass


    def test(self, response):
        print("CRAWLER BASIC IS WORKING")

    def addLink(self, next_page, checkPrefix=False):

        linkFound = False

        for link in self.linksQueue:
            if link.rstrip('/') == next_page.rstrip('/') or (checkPrefix and (link.find(next_page) >=0 or next_page.find(link) )):
                linkFound = True
                break

        if linkFound == False:
            self.linksQueue.append(next_page)

    def start_requests(self):
        print("URL TO BE PROCESSED", self.start_urls)

        self.linksQueue = []

        # for url in self.start_urls:
        #     print("processing url",url)
        #     self.addLink(url, True)
        #
        # for url in self.start_urls:
        #     self.linksQueueIndex += 1

        self.addLink(self.start_urls[0], True)
        yield scrapy.Request(url=self.linksQueue[self.linksQueueIndex - 1], callback=self.parse)


            # if self.MAXIMUM_NUMBER_PAGES != 0 and index == self.MAXIMUM_NUMBER_PAGES:
            #     index = 0
            #
            # print(index, len(self.linksQueue))

    def parse(self, response):

        url = response.url

        if self.testingURL != '':
            response = LinksHelper.getRequestTrials(self.session, self.testingURL, {}, {}, maxTrials = 5)
            html = response.text
            response = Selector(text=html)
            url = self.testingURL

        self.parseResponse(response, url)

        print(url, "data", response, self.ONLY_ONE_PAGE)

        if self.ONLY_ONE_PAGE == False:

            for next_page in response.css('a'):

                next_page = self.extractFirstElement(next_page.xpath('@href'))

                sharpIndex = next_page.find('#')
                if sharpIndex >= 0:
                    next_page = next_page[0: sharpIndex]

                parsed_url = urlparse(next_page)

                if bool(parsed_url.scheme) == False:
                    newUrl = self.url.rstrip('/')
                    newUrl = newUrl.rstrip('/')
                    next_page = newUrl + next_page

                # print(next_page)

                if self.MAXIMUM_NUMBER_PAGES == 0 or len(self.linksQueue) < self.MAXIMUM_NUMBER_PAGES:
                    self.addLink(next_page)

            try:

                while self.linksQueueIndex < len(self.linksQueue):

                    self.linksQueueIndex += 1

                    # print("self.linksQueue", len(self.linksQueue) )
                    # print("self.linksQueue[self.linksQueueIndex]", self.linksQueue[self.linksQueueIndex])

                    yield scrapy.Request(url=self.linksQueue[self.linksQueueIndex-1], callback=self.parse)

            except ValueError:
                pass




    def parseResponse(self, response, url):
        #print("prase function", url)

        LinksDB.addLinkVisited(self.domain, url)

        for rejection in self.rejectionSubstr:
            if rejection in url:
                return None

        self.crawlerProcess(response, url)

        self.toString()

        self.processScrapedData(url)

    def processScrapedData(self, url):
        pass

    def createParents(self):
        pass

    def getNextPages(self, response):
        pass


    def validate(self):
        return ''

    def toString(self):

        print("url", self.currentPageURL)
        if len(self.title) > 0: print("title:", self.title)
        if len(self.shortDescription) > 0: print("shortDescription:", self.shortDescription)
        if len(self.fullDescription) > 0: print("fullDescription:", self.fullDescription)
        if len(self.language) > 0: print("language:", self.language)
        if len(self.images) > 0: print("images:", self.images)
        if len(self.keywords) > 0: print("keywords:", self.keywords)

        if self.date is not None and self.date != '': print("date:", self.date)

        # print("og:title", self.ogTitle)
        # print("og:description", self.ogDescription)
        # print("og:image", self.ogImage)
        # print("og:site_name", self.ogSiteName)
        # print("page_url", self.currentPageURL)

        print("url:", self.currentPageURL)
        print("validate", self.validate())

    def toJSON(self):
        return {
            "title": self.title,
            "shortDescription": self.shortDescription,
            "fullDescription": self.fullDescription,
            "language": self.language,
            "images": self.images,
            "keywords": self.keywords,
            "date": self.date,
            "url": self.currentPageURL,
            "validate": self.validate()
        }

    def cleanText(self, text):
        return text
