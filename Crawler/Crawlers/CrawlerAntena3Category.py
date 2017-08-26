from Crawler.CrawlerBasic import CrawlerBasic

class CrawlerAntena3Category(CrawlerBasic):

    name = 'CrawlerAntena3Category'

    url = 'http://antena3.ro'
    domain = 'antena3.ro'

    start_urls = (url,)
    allowed_domains = [domain]

    def crawlerProcess(self, response):
        self.title = self.extractFirstElement(response.css('div.header-categorie h1::text'))

    def validate(self):
        if len(self.title) > 0:
            return 'category'

        return ''