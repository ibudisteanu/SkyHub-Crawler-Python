import dateparser

from Crawler.Crawlers.Interfaces.CrawlerNews import CrawlerNews


class CrawlerAntena3(CrawlerNews):

    name = 'CrawlerAntena3'

    url = 'https://antena3.ro'
    domain = 'antena3.ro'

    start_urls = (url,)
    allowed_domains = [domain]


    cssAuthor = 'div.autor-ora-comentarii span.fl a::text'
    cssAuthorLink = 'div.autor-ora-comentarii span.fl a::attr(href)'

    cssDateText = 'span.fl::text'

    cssFullDescription = 'div.articol div.text'

