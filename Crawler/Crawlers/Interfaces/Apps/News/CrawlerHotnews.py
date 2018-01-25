import dateparser

from Crawler.Crawlers.Interfaces.CrawlerNews import CrawlerNews


class CrawlerHotnews(CrawlerNews):

    name = 'CrawlerHotnews'

    url = 'https://hotnews.ro'
    domain = 'hotnews.ro'

    start_urls = (url,)
    allowed_domains = [domain]


    cssAuthor = 'div.autor a::text'
    cssAuthorLink = 'div.autor a::attr(href)'

    cssDateText = 'div.articol_render span.data::text'

    cssFullDescription = '#articleContent'

    websiteImage = "https://www.activenews.ro/images/articole/112207.png"
    websiteCover = "http://media.hotnews.ro/media_server1/image-2018-01-15-22225422-0-nokia-8.jpg"

