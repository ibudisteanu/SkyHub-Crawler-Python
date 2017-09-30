from Crawler.Helpers.LinksHelper import LinksHelper

class ObjectProductPrice:

    listPrice = ''
    youSave = ''

    watching = 0

    price = 0
    currency = ''

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

        print("   Quantity Sold", self.quantitySold)
        print("   Quantity Available", self.quantityAvailable)

    def calculateCurrency(self):

        if self.price is string
        string = self.price
        results = currencyconverter.parseString(string)

        self.price.replace("EUR", "€")
        self.price.replace("GBP", "€")

    def getJSON(self):

        return {
            'listPrice':self.listPrice,
            'youSave': self.youSave,
            'watching': self.watching,
            'price': self.price,
            'currency': self.currency,
            'quantityAvailable': self.quantityAvailable,
            'quantitySold': self.quantitySold,
        }