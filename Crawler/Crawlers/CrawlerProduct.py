import dateparser

from Crawler.CrawlerProcess import CrawlerProcess


class CrawlerProduct(CrawlerProcess):

    name = 'CrawlerEbay'

    url = 'http://ebay.com'
    domain = 'ebay.com'

    start_urls = (url,)
    allowed_domains = [domain]

    cssTitle = "#itemTitle::text"
    cssItemCondition = "#vi-itm-cond::text"
    cssTimeLeft = "span.vi-tm-left noscript"
    cssShippingSummary = "#delSummary::text"

    cssQuantityAvailable = "#qtySubTxt span::text"

    cssItemSpecifications = "div.itemAttr "
    #cssItemConditionDetails = "#vi-cond-addl-info"
    cssItemConditionDetails = ""
    #cssItemBrand = "tr td h2 span"
    cssItemBrand = ""
    #cssItemMaterial = ""
    cssItemMaterial = ""

    cssFullDescription = "desc_wrapper_ctr"

    cssAuthor = "span.mbg-nw::text"
    cssAuthorLink = "#mbgLink::attr(href)"

    cssAuthorScore = "span.mbg-l a::text"
    cssAuthorFeedbackOverall = "#si-fb::text"

    cssItemId = "#descItemNumber::text"

    cssDateText = ""
    cssDate = ""

    cssImages = "td.tdThumb div img"

    cssBreadcrumbsChildren = "td.vi-VR-brumblnkLst table tbody tr td h2 ul li"

    cssShipping = ""

    removeShortDescription = True



    # variables

    itemCondition = ''
    itemSpecifications = ''
    itemConditionDetails = ''
    itemBrand = ''
    itemMaterial = ''

    timeLeft = ''
    shippingSummary = ''
    shipping = []

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

        if self.cssQuantityAvailable != '':
            self.quantityAvailable = self.extractFirstElement(response.css(self.cssQuantityAvailable))

        if self.cssShippingSummary != '':
            self.shippingSummary = self.extractFirstElement(response.css(self.cssQuantityAvailable))

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
            if self.cssDate != '':
                self.date = self.extractFirstElement(response.css(self.cssDate))

        if self.cssImages != '':
            self.images = response.css(self.cssImages+"::attr(href)")

        if self.cssBreadcrumbsChildren != '':
            for i in reversed(range(1, 100)):
                parent = response.css(self.cssBreadcrumbsChildren + ':nth-child(' + str(i) + ')')
                parentText = self.extractFirstElement(parent.css('::text'))
                parentURL = self.extractFirstElement(parent.css('::attr(href)'))

                if parentText != '':
                    self.parents.append({'name': parentText, 'url': parentURL, 'index': i})

        self.parents = list(reversed(self.parents))  # changing the order




    def validate(self):
        if (len(self.title) > 3) and (len(self.fullDescription) > 40):
            return 'product'

        return ''

    def toStringAdditional(self):

        if len(self.itemCondition) > 0: print("Item Condition", self.itemCondition)
        if len(self.itemSpecifications) > 0: print("Item Specs", self.itemSpecifications)
        if len(self.itemConditionDetails) > 0: print("Item Condition Details", self.itemConditionDetails)
        if len(self.itemBrand) > 0: print("Item Brand", self.itemBrand)
        if len(self.itemMaterial) > 0: print("Item Material", self.itemMaterial)
        if len(self.timeLeft) > 0: print("Time Left", self.timeLeft)
        if len(self.authorScore) > 0: print("Author Score", self.authorScore)
        if len(self.authorFeedbackOverall) > 0: print("Author Feedback Overall", self.authorFeedbackOverall)
        if len(self.itemId) > 0: print("Item ID", self.itemId)
        if len(self.quantityAvailable) > 0: print("Quantity Available", self.quantityAvailable)

        if len(self.images) > 0: print("Images", self.images)
        if len(self.shippingSummary) > 0: print("Shippinh Summary", self.shippingSummary)
        if len(self.shipping) > 0: print("Shipping", self.shipping)