import dateparser

from Crawler.Crawlers.Interfaces.CrawlerNews import CrawlerNews


class CrawlerEvent(CrawlerNews):

    name = 'CrawlerBlog'

    url = 'http://fonduri-ue.ro'
    domain = 'fonduri-ue.ro'

    start_urls = (url,)
    allowed_domains = [domain]

    cssTitle = "h1.article-title a::attr(title)"
    cssAuthor = "div.postbody"
    cssAuthorLink = "div.postauthor"
    cssFullDescription = "section p"

    cssParent = "dd.category-name a"

    removeShortDescription = True

    def crawlerProcess(self, response, url):

        super().crawlerProcess(response, url)


    def validate(self):
        if (len(self.title) > 3) and (len(self.fullDescription) > 40):
            return 'news'

        return ''