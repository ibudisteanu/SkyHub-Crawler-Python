import dateparser
import datetime

from Crawler.Crawlers.CrawlerProcess import CrawlerProcess
from Crawler.Helpers.LinksDB import LinksDB
from Crawler.Objects.Products.ObjectRatingScore import ObjectRatingScore
from Crawler.Objects.Products.ObjectReview import ObjectReview

from Crawler.Objects.ObjectLink import ObjectLink
from Server.ServerAPI import ServerAPI

class CrawlerNews(CrawlerProcess):

    name = 'CrawlerNews'

    url = 'http://website.com'
    domain = 'website.com'

    start_urls = (url,)
    allowed_domains = [domain]

    replies = []

    def crawlerProcess(self, response, url):

        self.date = None
        super().crawlerProcess(response, url)

        keywordsArray =  self.keywords.split(',')

        if self.cssParent == '' and len(keywordsArray) > 1:
            self.parents.append({'name': '', 'url': self.url}) # parent and last keyword
            self.parents.append({'name': keywordsArray[0], 'url': url, 'index': 1})



    def validate(self):
        if len(self.title) > 3 and len(self.fullDescription) > 40 and (self.date is not None and self.date != ''):
            return 'news'

        return ''

    def checkDateLastDays(self, date, days):

        if date is None or self.date == '': return False

        today = datetime.datetime.now()
        diff = today - date

        if diff.days <= days: return True
        else: return False

    # Process Data and Create new Objects
    def processScrapedData(self, url):

        super().processScrapedData(url)

        # validate
        validation = self.validate()

        # topic
        if validation in ['news', 'topic']:

            title = self.title or self.ogTitle
            description = self.fullDescription or self.ogDescription or self.shortDescription

            topicObject = LinksDB.findLinkObjectAlready(self.domain, self.currentPageURL, title=title, description='', allowTitleIncluded=True, similarity=True)

            if topicObject is None:  # we have to add the topic

                if len(title) < 5 or len(description) < 30 : print("title or description are not good")
                elif self.checkDateLastDays(self.date, days=1) == False: print("last days")
                else:
                    topicId = ServerAPI.postAddTopic(self.url, url, self.user, self.parentId,
                                                     title,
                                                     description,
                                                     self.ogDescription or self.shortDescription,
                                                     self.keywords, self.images, self.date,
                                                     self.websiteCountry or self.language, self.websiteCity,
                                                     self.websiteLanguage or self.language, -666, -666,
                                                     self.author, self.authorAvatar)

                    topicObject = ObjectLink(self.currentPageURL, 'topic', topicId, self.title, self.parentId)
                    LinksDB.addLinkObject(self.domain, topicObject)

            else: print("News Already found")

            if topicObject is not None:

                topicId = topicObject.id
                print("new topic ", topicId)

                if len(self.replies) > 0:
                    for reply in self.replies:
                        replyObjectURL = self.currentPageURL + reply['title'] + reply['description']
                        replyObjectTitle = reply['title'] + reply['description']

                        replyObject = LinksDB.findLinkObjectAlready(self.domain, replyObjectURL, title=replyObjectTitle, description='', allowTitleIncluded=True)

                        if replyObject is None:  # we have to add the reply

                            if len(reply['description']) > 40:
                                replyId = ServerAPI.postAddReply(self.url, self.user, topicId,
                                                                 "", reply['title'], reply['description'],
                                                                 '', [], reply['date'],
                                                                 self.websiteCountry or self.language,
                                                                 self.websiteCity,
                                                                 self.websiteLanguage or self.language, -666, -666,
                                                                 reply['author'], reply['authorAvatar'])

                                replyObject = ObjectLink(replyObjectURL, 'reply', replyId, replyObjectTitle,
                                                         topicId)
                                LinksDB.addLinkObject(self.domain, replyObject)

                        if replyObject is not None:
                            replyId = replyObject.id
                            print("new reply ", replyId)

    def toString(self):

        super().toString()

        if len(self.replies) > 0: print("replies", self.replies)

    def toJSON(self):

        json = super().toJSON()
        if len(self.replies) > 0: json.replies = self.replies

        return json