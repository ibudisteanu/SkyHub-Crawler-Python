from Crawler.Crawlers.Interfaces.CrawlerNews import CrawlerNews

class CrawlerAntena3Category(CrawlerNews):

    name = 'CrawlerAntena3Category'

    url = 'http://antena3.ro'
    domain = 'antena3.ro'

    start_urls = (url,)
    allowed_domains = [domain]

    cssTitle = 'div.header-categorie h1::text'

    def crawlerProcess(self, response, url):
        super().crawlerProcess(response, url)


    def validate(self):
        if len(self.title) > 0:
            return 'category'

        return ''