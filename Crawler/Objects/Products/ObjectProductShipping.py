from Crawler.Helpers.LinksHelper import LinksHelper
from Crawler.Objects.Products.ObjectProductShippingCosts import ObjectProductShippingCosts

class ObjectProductShipping:

    url = ''

    itemLocation = ''


    shippingTo = []
    shippingExcludes = []

    # {'quantity':1, 'country':0, 'price':0, 'service': 'Economy Int Shipp', 'delivery*':'Estimated between Tue. Oct. 10 and Fri. Oct. 27'}
    shippingCosts = []

    lastUpdate = 0

    returnPolicy = ''
    shippingSummary = ''
    shippingDetails = ''

    def __init__(self, url, itemLocation, shippingTo, shippingExcludes, shippingCosts, shippingDetails, shippingSummary, returnPolicy, lastUpdate):

        self.url = url
        self.url = LinksHelper.fix_url(self.url)

        self.itemLocation = itemLocation
        self.shippingTo = shippingTo
        self.shippingExcludes = shippingExcludes
        self.shippingCosts = shippingCosts

        self.shippingDetails = shippingDetails
        self.shippingSummary = shippingSummary

        self.returnPolicy = returnPolicy
        self.lastUpdate = lastUpdate

    def toString(self):
        if len(self.itemLocation) > 0: print("   ", self.itemLocation)
        if len(self.shippingTo) > 0: print("   ", self.shippingTo)
        if len(self.shippingExcludes) > 0: print("   ", self.shippingExcludes)

        if len(self.shippingCosts) > 0:
            for i, shippingCost in enumerate(self.shippingCosts):
                print("   Shipping Cost")
                shippingCost.toString()

        if len(self.shippingDetails) > 0: print("   ", self.shippingDetails)
        if len(self.returnPolicy) > 0: print("   ", self.returnPolicy)
        if len(self.shippingSummary) > 0: print("   ", self.shippingSummary)
        if len(self.returnPolicy) > 0: print("   ", self.returnPolicy)
        if len(self.lastUpdate) > 0: print("   ", self.lastUpdate)
