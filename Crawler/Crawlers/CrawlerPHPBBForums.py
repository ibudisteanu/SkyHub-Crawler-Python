from Crawler.CrawlerBasic import CrawlerBasic

class CrawlerPHPBBForums(CrawlerBasic):

    name = 'CrawlerPHPForums'

    url = 'http://antena3.ro'
    domain = 'antena3.ro'

    start_urls = (url,)
    allowed_domains = [domain]

    def crawlerProcess(self, response):

        for i in range(100, 1):
            self.title = self.extractFirstElement(response.css('p.breadcrumbs > a:nth-child('+str(i)+')'))

            if self.title is not None:
                self.parent = self.extractFirstElement(response.css('p.breadcrumbs > a:nth-child(' + str(i-1) + ')'))
                if self.parent is not None:
                    self.parentIndex = i
                    break


    def validate(self):
        if len(self.title) > 0:
            return 'forum'

        return ''