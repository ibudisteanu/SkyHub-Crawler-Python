from Crawler.Helpers.LinksHelper import LinksHelper

class ObjectProductShippingCosts:

    url = ''

    itemLocation = ''
    shippingTo = ''

    lastUpdate = 0

    def __init__(self, shippingTo, shippingQuantity, shippingPrice, shippingService, shippingDelivery, returnPolicy, shippingText, lastUpdate):

        self.shippingTo = shippingTo
        self.shippingQuantity = shippingQuantity
        self.shippingPrice = shippingPrice
        self.shippingService = shippingService
        self.shippingDelivery = shippingDelivery
        self.returnPolicy = returnPolicy
        self.shippingText = shippingText

        self.lastUpdate = lastUpdate

    def toString(self):

        if len(self.shippingTo) > 0: print("   ", self.shippingTo)
        if len(self.shippingQuantity) > 0: print("   ", self.shippingQuantity)
        if len(self.shippingPrice) > 0: print("   ", self.shippingPrice)
        if len(self.shippingService) > 0: print("   ", self.shippingService)
        if len(self.shippingDelivery) > 0: print("   ", self.shippingDelivery)
        if len(self.returnPolicy) > 0: print("   ", self.returnPolicy)
        if len(self.shippingText) > 0: print("   ", self.shippingText)
        if len(self.lastUpdate) > 0: print("   ", self.lastUpdate)
