import dateparser

from Crawler.Crawlers.CrawlerProcess import CrawlerProcess


class CrawlerAntena3(CrawlerProcess):

    name = 'CrawlerAntena3'

    url = 'http://antena3.ro'
    domain = 'antena3.ro'

    start_urls = (url,)
    allowed_domains = [domain]

    def crawlerProcess(self, response, url):
        super().crawlerProcess(response, url)

        self.author = self.extractFirstElement(response.css('div.autor-ora-comentarii span.fl a::text'))
        self.authorLink = self.extractFirstElement(response.css('div.autor-ora-comentarii span.fl a::attr(href)'))

        self.fullDescription = ''.join(response.xpath("//div[@class='text']").extract())

        text = ''.join(response.xpath("//div[@class='autor-ora-comentarii']//text()").extract()).strip()
        self.date = dateparser.parse(text)


    def validate(self):
        if (len(self.title) > 3) and (len(self.shortDescription) > 3) and (len(self.fullDescription) > 10):
            return 'news'

        return ''