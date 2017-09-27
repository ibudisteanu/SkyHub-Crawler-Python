from Crawler.Helpers.LinksHelper import LinksHelper

class ObjectProductPrice:

    listPrice = ''
    youSave = ''

    watching = 0

    price = 0
    currency = ''

    self.quantityAvailable, self.quantitySold

    quantityAvailable = 0
    quantitySold = 0

    lastUpdate = 0

    def __init__(self, listPrice='', youSave='', price=0, currency='', watching='', quantityAvailable=0, quantitySold=0, lastUpdate='' ):

        self.listPrice = listPrice
        self.youSave = youSave
        self.price = price
        self.currency = currency
        self.watching = watching
        self.lastUpdate = lastUpdate

        self.quantityAvailable = quantityAvailable
        self.quantitySold = quantitySold


    def toString(self):

        if len(self.listPrice) > 0: print("   List Price", self.listPrice)
        if len(self.youSave) > 0: print("   You Save", self.youSave)
        print("   Price", self.price)
        if len(self.watching) > 0: print("   Watching", self.watching)