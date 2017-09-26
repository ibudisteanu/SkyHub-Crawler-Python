import dateparser

from Crawler.Crawlers.CrawlerProcess import CrawlerProcess
from Crawler.Helpers.LinksDB import LinksDB

from Crawler.Objects.Products.ObjectProduct import ObjectProduct
from Crawler.Objects.Products.ObjectProductShipping import ObjectProductShipping
from Crawler.Objects.Products.ObjectProductShippingCosts import ObjectProductShippingCosts

from Crawler.Objects.Products.ObjectReviewsScore import ObjectReviewScore
from Crawler.Objects.Products.ObjectReview import ObjectReview
from Crawler.Objects.Products.ObjectProductPrice import ObjectProductPrice

from Server.ServerAPI import ServerAPI


class CrawlerProduct(CrawlerProcess):

    name = 'CrawlerEbay'

    url = 'http://ebay.com'
    domain = 'ebay.com'

    testingURL =  "http://www.ebay.com/itm/50g-mechanic-soldering-solder-welding-paste-flux-mcn-300-smd-smt-sn63-pb37-new/171150278650"

    start_urls = (url,)
    allowed_domains = [domain]

    availableToBuy = True
    cssAvailableToBuy = "#binBtn_btn"

    cssTitle = "#itemTitle::text"
    cssItemCondition = "#vi-itm-cond::text"
    cssTimeLeft = "span.timeMs::attr(timems)"


    cssShippingSummary = "#shSummary"
    cssShippingText = "#shipNHadling"
    cssShippingItemLocation = "#itemLocation div div div.iti-eu-bld-gry span::text"
    cssShippingTo = "#sh-gsp-wrap div.sh-sLoc:nth-child(1)::text"
    cssShippingExcludes = "#sh-gsp-wrap div.sh-sLoc:last-child::text"

    cssQuantityAvailable = "#qtySubTxt span::text"
    cssQuantitySold = "span.vi-qtyS-hot-red.vi-qty-vert-algn.vi-qty-pur-lnk a::text"

    cssItemSpecifications = "div.itemAttr "
    #cssItemConditionDetails = "#vi-cond-addl-info"
    cssItemConditionDetails = ""
    #cssItemBrand = "tr td h2 span"
    cssItemBrand = ""
    #cssItemMaterial = ""
    cssItemMaterial = ""

    cssFullDescription = "#desc_div"

    cssAuthor = "span.mbg-nw::text"
    cssAuthorLink = "#mbgLink::attr(href)"

    cssAuthorScore = "span.mbg-l a::text"
    cssAuthorFeedbackOverall = "#si-fb::text"

    cssItemId = "#descItemNumber::text"

    cssDateText = ""
    cssDate = ""

    cssImages = "td.tdThumb div img"

    cssBreadcrumbsChildrenList = "#vi-VR-brumb-lnkLst table tr td h2 ul li"
    cssBreadcrumbsChildrenListElementHref = 'a'
    cssBreadcrumbsChildrenListElement = 'a span'

    removeShortDescription = True


    cssListPrice = "#orgPrc::text"
    cssYouSave ="#youSaveSTP::text"
    cssPrice = "#prcIsum::text"
    cssWatching = "span.vi-buybox-watchcount::text"

    cssRatingScoresList = "ul.ebay-review-list li.ebay-review-item"
    cssRatingScoresListElementValue = "p.ebay-review-item-stars::text"
    cssRatingScoresListElementScore = "p.ebay-review-item-stars::text"

    cssReviewsList = "div.reviews div.ebay-review-section"
    cssReviewsListElementUsername = "div a::text"
    cssReviewsListElementDate = "div.ebay-review-section-l span::text"
    cssReviewsListElementRatingScore = ""
    cssReviewsListElementRatingScoreStars = "div div span i.fullStar"
    cssReviewsListElementTitle = "div p.review-item-title::text"
    cssReviewsListElementBody = "div p.review-item-content"
    cssReviewsListElementPurchased = "div p.review-attr"
    cssReviewsListElementThumbsUp = "div.review-btns div a span.review-section-rr-txt span.positive-h-c::text"
    cssReviewsListElementThumbsDown = "div.review-btns div a span.review-section-rr-txt span.negative-h-c::text"


    # variables

    itemCondition = ''
    itemSpecifications = ''
    itemConditionDetails = ''
    itemBrand = ''
    itemMaterial = ''

    timeLeft = ''
    shipping = None

    authorScore = 0
    authorFeedbackOverall = 0

    itemId = ''
    quantityAvailable = 0
    quantitySold = 0

    price = None

    ratingScoresList = []
    ratingsTotal = 0

    reviewsList = []

    def crawlerProcess(self, response, url):

        super().crawlerProcess(response, url)

        if self.removeShortDescription:
            self.shortDescription = ''
            self.ogDescription = ''

        if self.cssTitle != '':
            self.title = self.extractText(response.css(self.cssTitle))

        if self.cssItemCondition != '':
            self.itemCondition = self.extractText(response.css(self.cssItemCondition))

        if self.cssTimeLeft != '':
            self.timeLeft = self.extractText(response.css(self.cssTimeLeft))

        if self.cssQuantityAvailable != '':
            self.quantityAvailable = self.extractText(response.css(self.cssQuantityAvailable))

        if self.cssQuantitySold != '':
            self.quantitySold = self.extractText(response.css(self.cssQuantitySold))

        if self.cssShippingSummary != '' or self.cssShippingText != '':

            self.shipping = ObjectProductShipping()

            if self.cssShippingSummary != '':
                self.shipping.shippingSummary = self.extractText(response.css(self.cssShippingSummary))

            if self.cssShippingText != '':
                self.shipping.text = self.extractText(response.css(self.cssShippingText))

            if self.cssShippingItemLocation != '':
                self.shipping.itemLocation = self.extractText(response.css(self.cssShippingItemLocation))

            if self.cssShippingTo != '':
                self.shipping.shippingTo = self.extractText(response.css(self.cssShippingTo))

            if self.cssShippingExcludes != '':
                self.shipping.shippingExcludes = self.extractText(response.css(self.cssShippingExcludes))


        if self.cssItemSpecifications != '':
            self.itemSpecifications = self.extractText(response.css(self.cssItemSpecifications))

        if self.cssItemConditionDetails != '':
            self.itemConditionDetails = self.extractText(response.css(self.cssItemConditionDetails))

        if self.cssItemBrand != '':
            self.itemBrand = self.extractText(response.css(self.cssItemBrand))

        if self.cssItemMaterial != '':
            self.itemMaterial = self.extractText(response.css(self.cssItemMaterial))

        self.fullDescription = self.extractText(response.css(self.cssFullDescription))

        if self.cssAuthor != '':
            self.author = self.extractText(response.css(self.cssAuthor))

        if self.cssAuthorLink != '':
            self.authorLink = self.extractText(response.css(self.cssAuthorLink))

        if self.cssAuthorScore != '':
            self.authorScore = self.extractText(response.css(self.cssAuthorScore))

        if self.cssAuthorFeedbackOverall != '':
            self.authorFeedbackOverall = self.extractText(response.css(self.cssAuthorFeedbackOverall))

        if self.cssItemId != '':
            self.itemId = self.extractText(response.css(self.cssItemId))

        if self.cssDateText != '':  #text format like 22 Jul 2017
            date = self.extractText(response.css(self.cssDate))
            print("DATEEE",date)
            self.date = dateparser.parse(date)
        else: #timestamp format
            if self.cssDate != '':
                self.date = self.extractText(response.css(self.cssDate))

        if self.cssImages != '':
            self.images = []

            images = response.css(self.cssImages)
            for i, image in enumerate(images):
                imageSrc = image.css('::attr(src)').extract_first()
                imageAlt = image.css('::attr(alt)').extract_first()

                self.images.append({'src': imageSrc, 'alt': imageAlt})

        if self.cssListPrice != '' or self.cssPrice != '' or self.cssYouSave != '' or self.cssWatching != '':

            self.price = ObjectProductPrice()

            if self.cssListPrice != '': self.price.listPrice = self.extractText(response.css(self.cssListPrice))
            if self.cssYouSave != '': self.price.youSave = self.extractText(response.css(self.cssYouSave))
            if self.cssPrice != '': self.price.price = self.extractText(response.css(self.cssPrice))
            if self.cssWatching != '': self.price.watching = self.extractText(response.css(self.cssWatching))


        if self.cssAvailableToBuy != '':
            self.availableToBuy = False
            if len(response.css(self.cssAvailableToBuy)) >0:
                self.availableToBuy = True

        # raiting scores
        if self.cssRatingScoresList != '' and len(self.title) > 0:

            self.ratingScoresList = []
            self.ratingsTotal = 0

            ratingScoreList = response.css(self.cssRatingScoresList)

            # print("!!!!!!!!!!!!!!!!!!! total", self.cssRatingScoresList, ratingScoreList)

            count = 0
            for i, ratingScoreObject in  enumerate(ratingScoreList):

                # print( "!!!!!!!!!!!!!!!!!!!", ratingScoreObject )

                ratingScore = self.extractText( ratingScoreObject.css(self.cssRatingScoresListElementScore) )
                ratingValue = self.extractText( ratingScoreObject.css(self.cssRatingScoresListElementValue) )

                print("ratingScore", ratingScore, ratingValue)

                if ratingScore != '' and ratingValue != '':
                    ratingScore = int(ratingScore)
                    ratingValue = int(ratingValue)

                    self.ratingScoresList.append(ObjectReviewScore(ratingScore, ratingValue))

                    self.ratingsTotal += ratingScore * ratingValue
                    count += ratingScore

            if count > 0:
                self.ratingsTotal /= count


        # reviews
        if self.cssReviewsList != '' and len(self.title) > 0:

            self.reviewsList = []

            reviewList = response.css( self.cssReviewsList )

            print("@@@@@@@@@@@@@@@  total", reviewList)
            for i, reviewObject in enumerate(reviewList):

                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",reviewObject)

                reviewUsername = self.extractText(reviewObject.css(self.cssReviewsListElementUsername))
                reviewFullName = ''

                reviewDate = self.extractText(reviewObject.css(self.cssReviewsListElementDate))
                reviewTitle = self.extractText(reviewObject.css(self.cssReviewsListElementTitle))
                reviewBody = self.extractText(reviewObject.css(self.cssReviewsListElementBody))

                if self.cssReviewsListElementRatingScore != '':
                    reviewScore = self.extractText(reviewObject.css(self.cssReviewsListElementRatingScore))

                if self.cssReviewsListElementRatingScoreStars != '': #with stars
                    reviewScore = len(reviewObject.css(self.cssReviewsListElementRatingScoreStars))

                reviewPurchased = self.extractText(reviewObject.css(self.cssReviewsListElementPurchased))
                reviewThumbsUp = self.extractText(reviewObject.css(self.cssReviewsListElementThumbsUp))
                reviewThumbsDown = self.extractText(reviewObject.css(self.cssReviewsListElementThumbsDown))

                reviewScore = int(reviewScore)
                reviewThumbsUp = int(reviewThumbsUp)
                reviewThumbsDown = int(reviewThumbsDown)

                # print("review username ", reviewUsername)
                # print("review fullname ", reviewFullName)
                # print("review date ", reviewDate)
                # print("review title ", reviewTitle)
                # print("review body ", reviewBody)
                # print("review score ", reviewScore)
                # print("review purchased ", reviewPurchased)
                # print("review thumbs up ", reviewThumbsUp)
                # print("review thumbs down ", reviewThumbsDown)

                if (reviewBody != '' or reviewTitle != '') and reviewScore != '':
                    self.reviewsList.append(ObjectReview('', reviewUsername, reviewFullName, reviewDate, reviewScore, reviewTitle, reviewBody, reviewPurchased, reviewThumbsUp, reviewThumbsDown, ))


    def validate(self):
        if (len(self.title) > 3) and (len(self.fullDescription) > 40) and self.availableToBuy:
            return 'product'

        return ''

    def toString(self):

        super().toString()


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
        if len(self.quantitySold) > 0: print("Quantity Sold", self.quantitySold)

        if len(self.images) > 0: print("Images", self.images)

        if self.shipping is not None:
            print("Shipping Summary")
            self.shipping.toString()

        if self.price is not None:
            print("Price")
            self.price.toString()

        print("Rating Scores List", len(self.ratingScoresList))
        if len(self.ratingScoresList) >0:
            for i, rating in enumerate(self.ratingScoresList):
                print("Rating Scores List")
                rating.toString()

        print("ReviewList",len(self.reviewsList))
        if len(self.reviewsList) > 0:
            for i, review in enumerate(self.reviewsList):
                print("ReviewList")
                review.toString()

        print("Available To Buy", self.availableToBuy)


    # Process Data and Create new Objects
    def processScrapedData(self, url):

        super().processScrapedData(url)

        # validate
        validation = self.validate()

        # product
        if validation in ['product']:

            productObject = LinksDB.findLinkObjectAlready(self.domain, self.currentPageURL,
                                                          self.title or self.ogTitle, True)

            if productObject is None:  # we have to add the topic

                title = self.title or self.ogTitle
                description = self.fullDescription or self.ogDescription or self.shortDescription

                if len(title) > 5 and len(description) > 30:
                    productId = ServerAPI.postAddProduct(self.url, self.user, self.parentId,
                                                         title,
                                                         description,
                                                         self.ogDescription or self.shortDescription,
                                                         self.keywords, self.images, self.date,
                                                         self.websiteCountry or self.language, self.websiteCity,
                                                         self.websiteLanguage or self.language, -666, -666,
                                                         self.author, self.authorAvatar)

                    productObject = ObjectProduct(self.currentPageURL, 'product', self.itemId, productId, self.author, self.parents, self.title, self.timeLeft, self.itemCondition, self.itemSpecifications, self.itemConditionDetails, self.itemBrand, self.itemMaterial,
                                                  self.fullDescription, self.images, self.price, self.details, self.date, self.ratingsTotal, self.ratingScoresList, self.shipping , self.quantityAvailable, self.quantitySold,  self.reviewsList, self.lastUpdate)

                    LinksDB.addLinkObject(self.domain, productObject)
