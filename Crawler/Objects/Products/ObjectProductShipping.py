from Crawler.Helpers.LinksHelper import LinksHelper
from Crawler.Objects.Products.ObjectProductShippingCosts import ObjectProductShippingCosts

class ObjectProductShipping:

    itemLocation = ''


    shippingTo = []
    shippingExcludes = []

    # {'quantity':1, 'country':0, 'price':0, 'service': 'Economy Int Shipp', 'delivery*':'Estimated between Tue. Oct. 10 and Fri. Oct. 27'}
    shippingCosts = []

    lastUpdate = 0

    returnPolicy = ''
    summary = ''
    details = ''
    text = ''

    def __init__(self,  itemLocation='', shippingTo='', shippingExcludes='', shippingCosts='', details='', summary='', returnPolicy='', deliverySummary='', lastUpdate=''):

        self.itemLocation = itemLocation
        self.shippingTo = shippingTo
        self.shippingExcludes = shippingExcludes
        self.shippingCosts = shippingCosts

        self.details = details
        self.summary = summary

        self.returnPolicy = returnPolicy
        self.deliverySummary = deliverySummary

        self.lastUpdate = lastUpdate

    def toString(self):
        if len(self.itemLocation) > 0: print("   item location ", self.itemLocation)
        if len(self.shippingTo) > 0: print("   shipping to ", self.shippingTo)
        if len(self.shippingExcludes) > 0: print("   shippingExcludes ", self.shippingExcludes)

        if len(self.shippingCosts) > 0:
            for i, shippingCost in enumerate(self.shippingCosts):
                print("   Shipping Cost")
                shippingCost.toString()

        if len(self.details) > 0: print("   details ", self.details)
        if len(self.text) > 0: print("   text ", self.text)
        if len(self.returnPolicy) > 0: print("   return policy", self.returnPolicy)
        if len(self.summary) > 0: print("   summary ", self.summary)
        if len(self.deliverySummary) > 0: print("   delivery summary ", self.deliverySummary)
        if len(self.lastUpdate) > 0: print("   ", self.lastUpdate)


    def getJSON(self):

        data = {
            'itemLocation': self.itemLocation,
            'shippingTo':self.shippingTo,
            'shippingExcludes': self.shippingExcludes,

            'returnPolicy': self.returnPolicy,
            'summary': self.summary,
            'details': self.details,
            'text': self.text,
        }

        if len(self.shippingCosts) > 0:
            list = []
            for i, shippingCost in enumerate(self.shippingCosts):
                list.append(shippingCost.getJSON())

            data['shippingCosts'] = list

        return data