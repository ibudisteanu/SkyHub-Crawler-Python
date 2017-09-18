from Crawler.Helpers.LinksHelper import LinksHelper

class ObjectProduct:

    url = ''
    type = ''
    originalId = ''

    # objectId from SkyHub
    id = ''

    sellerUsername = '',

    categories = []

    title = ''

    timeLeft = ''
    itemCondition = ''

    itemSpecifications = ''

    itemConditionDetails = ''
    itemBrand = ''
    itemMaterial = ''

    description = ''

    images = []

    price = ''
    details = ''

    date = ''

    ratingsTotal = 0
    ratings = []

    deliverySummary = ''
    shipping = ''

    returnPolicy = ''

    quantityAvailable = 0
    quantitySold = 0

    reviews = []  # reviews array of Review

    lastUpdate = 0

    def __init__(self, url, type, originalId, id, sellerUsername, categories, title, timeLeft, itemCondition, itemSpecifications, itemConditionDetails, itemBrand, itemMaterial, description, images, price, details, date, ratingsTotal, ratings, deliverySummary, shipping, returnPolicy, quantityAvailable, quantitySold, reviews, lastUpdate ):

        self.url = url
        self.url = LinksHelper.fix_url(self.url)

        self.type = type
        self.originalId = originalId
        self.id = id
        self.sellerUsername = sellerUsername
        self.categories = categories
        self.title = title
        self.timeLeft = timeLeft

        self.itemCondition = itemCondition
        self.itemSpecifications = itemSpecifications
        self.itemConditionDetails = itemConditionDetails
        self.itemBrand = itemBrand
        self.itemMaterial = itemMaterial

        self.description = description
        self.images = images

        self.price = price
        self.details = details
        self.date = date
        self.ratingsTotal = ratingsTotal
        self.ratings = ratings
        self.returnPolicy = returnPolicy


        self.quantityAvailable = quantityAvailable
        self.quantitySold = quantitySold

        self.reviews = reviews
        self.lastUpdate = lastUpdate

        self.deliverySummary = deliverySummary
        self.shipping = shipping
