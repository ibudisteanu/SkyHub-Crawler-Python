import dateparser

from Crawler.Crawlers.Interfaces.CrawlerNews import CrawlerNews


class CrawlerAntena3(CrawlerNews):

    name = 'CrawlerAntena3'

    url = 'http://antena3.ro'
    domain = 'antena3.ro'

    start_urls = (url,)
    allowed_domains = [domain]

    cssAuthor = 'div.autor-ora-comentarii span.fl a::text'
    cssAuthorLink = 'div.autor-ora-comentarii span.fl a::attr(href)'

    cssFullDescription = 'div.articol div.text'

    def crawlerProcess(self, response, url):
        super().crawlerProcess(response, url)

        text = ''.join(response.xpath("//div[@class='autor-ora-comentarii']//text()").extract()).strip()
        self.date = dateparser.parse(text)


    def validate(self):
        if (len(self.title) > 3) and (len(self.shortDescription) > 3) and (len(self.fullDescription) > 10):
            return 'news'

        return ''