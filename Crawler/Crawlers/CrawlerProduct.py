import dateparser

from Crawler.CrawlerProcess import CrawlerProcess


class CrawlerEbay(CrawlerProcess):

    name = 'CrawlerEbay'

    url = 'http://ebay.com'
    domain = 'ebay.com'

    start_urls = (url,)
    allowed_domains = [domain]

    cssTitle = "#itemTitle"
    cssItemCondition = "#vi-itm-cond"
    cssTimeLeft = "span.vi-tm-left noscript"
    cssQuantityAvailable = "#qtySubTxt span"

    cssItemSpecifications = "div.itemAttr "
    #cssItemConditionDetails = "#vi-cond-addl-info"
    #cssItemBrand = "tr td h2 span"
    #cssItemMaterial = ""

    cssFullDescription = "desc_wrapper_ctr"

    cssAuthor = "span.mbg-nw"
    cssAuthorLink = "#mbgLink"

    cssAuthorScore = "span.mbg-l a"
    cssAuthorFeedbackOverall = "#si-fb"

    cssItemId = "#descItemNumber"

    cssDateText = ""
    cssDate = ""
    #cssDate = "time::attr(datetime)"

    cssParent = "dd.category-name a"

    removeShortDescription = True

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