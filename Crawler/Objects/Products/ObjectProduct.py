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
    details = None

    description = ''

    images = []

    price = None

    date = ''

    ratings = None

    shipping = None


    reviews = []  # reviews array of Review

    lastUpdate = 0

    def __init__(self, url, type, originalId, id, sellerUsername, categories, title,  description, images,
                 timeLeft, price, details, date, ratings, shipping, reviews, lastUpdate ):

        self.url = url
        self.url = LinksHelper.fix_url(self.url)

        self.type = type
        self.originalId = originalId
        self.id = id
        self.sellerUsername = sellerUsername
        self.categories = categories
        self.title = title
        self.timeLeft = timeLeft

        self.details = details

        self.description = description
        self.images = images

        self.price = price

        self.date = date
        self.ratings = ratings

        self.reviews = reviews
        self.lastUpdate = lastUpdate

        self.shipping = shipping
