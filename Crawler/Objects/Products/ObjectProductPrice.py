from Crawler.Helpers.LinksHelper import LinksHelper

class ObjectProductPrice:

    listPrice = ''
    youSave = ''

    watching = 0

    price = 0
    currency = ''

    lastUpdate = 0

    def __init__(self, listPrice='', youSave='', price=0, currency='', watching='', lastUpdate='' ):

        self.listPrice = listPrice
        self.youSave = youSave
        self.price = price
        self.currency = currency
        self.watching = watching
        self.lastUpdate = lastUpdate


    def toString(self):

        if len(self.listPrice) > 0: print("   List Price", self.listPrice)
        if len(self.youSave) > 0: print("   You Save", self.youSave)
        if len(self.price) > 0: print("   Price", self.price)
        if len(self.watching) > 0: print("   Watching", self.watching)