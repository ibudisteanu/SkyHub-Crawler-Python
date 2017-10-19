import dateparser

from Crawler.Crawlers.CrawlerProcess import CrawlerProcess
from Crawler.Helpers.LinksDB import LinksDB
from Crawler.Objects.Products.ObjectRatingScore import ObjectReviewScore
from Crawler.Objects.Products.ObjectReview import ObjectReview

class CrawlerNews(CrawlerProcess):

    name = 'CrawlerNews'

    url = 'http://website.com'
    domain = 'website.com'

    start_urls = (url,)
    allowed_domains = [domain]

    replies = []

    def crawlerProcess(self, response, url):

        super().crawlerProcess(response, url)




    def validate(self):
        if (len(self.title) > 3) and (len(self.fullDescription) > 40):
            return 'news'

        return ''

    # to string
    def toString(self):
        super().toString()

    # Process Data and Create new Objects
    def processScrapedData(self, url):

        super().processScrapedData(url)

        # validate
        validation = self.validate()

        # topic
        if validation in ['news', 'topic']:

            title = self.title or self.ogTitle
            description = self.fullDescription or self.ogDescription or self.shortDescription

            topicObject = LinksDB.findLinkObjectAlready(self.domain, self.currentPageURL, title=title, description='', allowTitleIncluded=True)

            if topicObject is None:  # we have to add the topic

                if len(title) > 5 and len(description) > 30:
                    topicId = ServerAPI.postAddTopic(self.url, self.user, self.parentId,
                                                     title,
                                                     description,
                                                     self.ogDescription or self.shortDescription,
                                                     self.keywords, self.images, self.date,
                                                     self.websiteCountry or self.language, self.websiteCity,
                                                     self.websiteLanguage or self.language, -666, -666,
                                                     self.author, self.authorAvatar)

                    topicObject = ObjectLink(self.currentPageURL, 'topic', topicId, self.title, self.parentId)
                    LinksDB.addLinkObject(self.domain, topicObject)

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
