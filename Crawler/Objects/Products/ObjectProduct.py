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
    description = ''
    price = ''
    details = ''

    date = ''

    ratingsTotal = 0
    ratings = []

    returnPolicy = ''

    stockAvailable = 0

    reviews = []  # reviews array of Review

    lastUpdate = 0

    def __init__(self, url, type, originalId, id, sellerUsername, categories, title, description, price, details, date, ratingsTotal, ratings, returnPolicy, stockAvailable, reviews, lastUpdate ):

        self.url = url
        self.url = LinksHelper.fix_url(self.url)

        self.type = type
        self.originalId = originalId
        self.id = id
        self.sellerUsername = sellerUsername
        self.categories = categories
        self.title = title
        self.description = description
        self.price = price
        self.details = details
        self.date = date
        self.ratingsTotal = ratingsTotal
        self.ratings = ratings
        self.returnPolicy = returnPolicy
        self.stockAvailable = stockAvailable
        self.reviews = reviews
        self.lastUpdate = lastUpdate
