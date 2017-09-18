import dateparser

from Crawler.Crawlers.CrawlerProcess import CrawlerProcess


class CrawlerBlog(CrawlerProcess):

    name = 'CrawlerBlog'

    url = 'http://fonduri-ue.ro'
    domain = 'fonduri-ue.ro'

    start_urls = (url,)
    allowed_domains = [domain]

    cssTitle = "h1.article-title a::attr(title)"
    cssAuthor = "div.postbody"
    cssAuthorLink = "div.postauthor"
    cssFullDescription = "section p"

    cssDateText = ""
    cssDate = "time::attr(datetime)"

    cssParent = "dd.category-name a"

    removeShortDescription = True

    def crawlerProcess(self, response, url):

        super().crawlerProcess(response, url)

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



        if self.cssDateText != '':  #text format like 22 Jul 2017
            date = ' '.join(response.css(self.cssDate).extract()).strip()
            print("DATEEE",date)
            self.date = dateparser.parse(date)
        else: #timestamp format
            if self.extractFirstElement(response.css(self.cssDate)) == '':
                self.fullDescription = ''
            else:
                self.date = self.extractFirstElement(response.css(self.cssDate))


        self.parents = []

        parent = response.css(self.cssParent)
        parentText = self.extractFirstElement(parent.css('::text'))
        parentURL = ' '.join((parent.css('::attr(href)').extract()))

        if parentText != '' and parentURL != '':
            self.parents.append({'name': parentText, 'url': parentURL, 'index': 1})

    def validate(self):
        if (len(self.title) > 3) and (len(self.fullDescription) > 40):
            return 'news'

        return ''