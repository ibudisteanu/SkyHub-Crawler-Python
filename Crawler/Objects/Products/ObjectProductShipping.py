from Crawler.Helpers.LinksHelper import LinksHelper

class ObjectProductShipping:

    url = ''

    itemLocation = ''
    shippingTo = ''
    shippingExcludes = []

    # {'quantity':1, 'country':0, 'price':0, 'service': 'Economy Int Shipp', 'delivery*':'Estimated between Tue. Oct. 10 and Fri. Oct. 27'}
    shippingCosts = []

    lastUpdate = 0

    def __init__(self, url, itemLocation, shippingTo, shippingExcludes, shippingCosts, lastUpdate):

        self.url = url
        self.url = LinksHelper.fix_url(self.url)

        self.itemLocation = itemLocation
        self.shippingTo = shippingTo
        self.shippingExcludes = shippingExcludes
        self.shippingCosts = shippingCosts
        self.lastUpdate = lastUpdate
