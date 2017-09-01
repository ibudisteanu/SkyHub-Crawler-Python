import dateparser

from Crawler.CrawlerBasic import CrawlerBasic


class CrawlerBlog(CrawlerBasic):

    name = 'CrawlerBlog'

    url = 'http://fonduri-ue.ro'
    domain = 'fonduri-ue.ro'

    start_urls = (url,)
    allowed_domains = [domain]

    cssTitle = "h1.article-title a::attr(title)"
    cssAuthor = "div.postbody"
    cssAuthorLink = "div.postauthor"
    cssFullDescription = "section p"
    cssDate = "time::attr(datetime)"
    cssParent = "dd.category-name a"

    removeShortDescription = True

    def setParams(self, url='', domain='', cssTitle='', cssAuthor='', cssAuthorLink='', cssFullDescription='', cssDate='', cssParent=''):

        if url != '':
            self.url = url
            self.start_urls = (url, )

        if domain != '':
            self.domain = domain
            self.allowed_domains = [domain]
        if cssTitle != '': self.cssTitle = cssTitle
        if cssAuthor != '': self.cssAuthor = cssAuthor


    def crawlerProcess(self, response, url):

        if self.removeShortDescription:
            self.shortDescription = ''
            self.ogDescription = ''

        if self.cssAuthor != '':
            self.author = self.extractFirstElement(response.css(self.cssAuthor))

        if self.cssAuthorLink != '':
            self.authorLink = self.extractFirstElement(response.css(self.cssAuthorLink))

        self.fullDescription = ''.join(response.css(self.cssFullDescription).extract()).strip()

        if self.cssTitle != '':
            self.title = self.extractFirstElement(response.css(self.cssTitle))

        text = ' '.join(response.css(self.cssDate).extract()).strip()
        print(text)
        self.date = dateparser.parse(text)

        parent = response.css(self.cssParent)
        parentText = self.extractFirstElement(parent.css('::text'))
        parentURL = ' '.join((parent.css('::attr(href)').extract()))

        if parentText != '' and parentURL != '':
            self.parents.append({'name': parentText, 'url': parentURL, 'index': 1})

    def validate(self):
        if (len(self.title) > 3) and (len(self.fullDescription) > 10):
            return 'news'

        return ''