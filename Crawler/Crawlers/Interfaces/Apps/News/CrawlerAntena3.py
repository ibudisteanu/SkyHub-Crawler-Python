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


    websiteImage = "https://www.antena3.ro/thumbs/big3/2017/01/30/antena-3-cel-mai-urmarit-post-de-stiri-in-29-ianuarie-431298.jpg"
    websiteCover = "http://promoa3.antena3.ro/wp-content/uploads/2012/06/IMG_2950-m.jpg"
    websiteLanguage = "RO"

