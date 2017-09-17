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
    cssItemConditionDetails = ""
    #cssItemBrand = "tr td h2 span"
    cssItemBrand = ""
    #cssItemMaterial = ""
    cssItemMaterial = ""

    cssFullDescription = "desc_wrapper_ctr"

    cssAuthor = "span.mbg-nw"
    cssAuthorLink = "#mbgLink"

    cssAuthorScore = "span.mbg-l a"
    cssAuthorFeedbackOverall = "#si-fb"

    cssItemId = "#descItemNumber"

    cssDateText = ""
    cssDate = ""

    cssImages = "td.tdThumb div img"

    cssCategories = "td.vi-VR-brumblnkLst table tbody tr td h2 ul li"

    removeShortDescription = True

    # variables

    itemCondition = ''
    itemSpecifications = ''
    itemConditionDetails = ''
    itemBrand = ''
    itemMaterial = ''

    timeLeft = ''

    authorScore = 0
    authorFeedbackOverall = 0

    itemId = ''
    quantityAvailable = 0

    def crawlerProcess(self, response, url):

        if self.removeShortDescription:
            self.shortDescription = ''
            self.ogDescription = ''

        if self.cssTitle != '':
            self.title = self.extractFirstElement(response.css(self.cssTitle))

        if self.cssItemCondition != '':
            self.itemCondition = self.extractFirstElement(response.css(self.cssItemCondition))

        if self.cssTimeLeft != '':
            self.timeLeft = self.extractFirstElement(response.css(self.cssTimeLeft))

        if self.cssQuantityAvailable != ''
            self.quantityAvailable = self.extractFirstElement(response.css(self.cssQuantityAvailable))

        if self.cssItemSpecifications != '':
            self.itemSpecifications = self.extractFirstElement(response.css(self.cssItemSpecifications))

        if self.cssItemConditionDetails != '':
            self.itemConditionDetails = self.extractFirstElement(response.css(self.cssItemConditionDetails))

        if self.cssItemBrand != '':
            self.itemBrand = self.extractFirstElement(response.css(self.cssItemBrand))

        if self.cssItemMaterial != '':
            self.itemMaterial = self.extractFirstElement(response.css(self.cssItemMaterial))

        self.fullDescription = ''.join(response.css(self.cssFullDescription).extract()).strip()

        if self.cssAuthor != '':
            self.author = self.extractFirstElement(response.css(self.cssAuthor))

        if self.cssAuthorLink != '':
            self.authorLink = self.extractFirstElement(response.css(self.cssAuthorLink))

        if self.cssAuthorScore != '':
            self.authorScore = self.extractFirstElement(response.css(self.cssAuthorScore))

        if self.cssAuthorFeedbackOverall != '':
            self.authorFeedbackOverall = self.extractFirstElement(response.css(self.cssAuthorFeedbackOverall))

        if self.cssItemId != '':
            self.itemId = self.extractFirstElement(response.css(self.cssItemId))

        if self.cssDateText != '':  #text format like 22 Jul 2017
            date = ' '.join(response.css(self.cssDate).extract()).strip()
            print("DATEEE",date)
            self.date = dateparser.parse(date)
        else: #timestamp format
            if self.extractFirstElement(response.css(self.cssDate)) == '':
                self.fullDescription = ''
            else:
                self.date = self.extractFirstElement(response.css(self.cssDate))

        if self.cssImages != '':
            cssImages = response.css(self.cssImages+"::attr(href)")

        if self.cssCategories != '':
            cssCategories = response.css(self.cssCategories)



    def validate(self):
        if (len(self.title) > 3) and (len(self.fullDescription) > 40):
            return 'product'

        return ''