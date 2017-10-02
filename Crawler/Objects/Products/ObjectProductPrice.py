from Crawler.Helpers.LinksHelper import LinksHelper
from Crawler.Objects.Products.Helpers.CurrencyConverter import parseString
#import Crawler.Objects.Products.Helpers.CurrencyConverter

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

    def setPrice(self, newPrice, newCurrency = ''):

        self.price = newPrice
        self.currency = newCurrency

        if newCurrency == '':
            self.calculateCurrency()

        return [self.price, self.currency]

    def calculateCurrency(self):

        if isinstance(self.price, str):

            self.price.replace("EUR", "€")
            self.price.replace("GBP", "£")
            self.price.replace("Can$", "CAD")
            self.price.replace("C$", "CAD")


            string = self.price
            results = parseString(string)

            print("DEBUG",string, results)

            # sample of results
            # [['USD',4430000],['GBP',400000]]

            if len(results) > 0:
                self.price = results[0][1]
                self.currency = results[0][0]

                if len(results) > 1:
                    print("WARNING!!! MORE THAN ONE PRICE FOUND", string)

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

    def testCurrencyConvertor(self):

        print(self.setPrice("$50"))
        print(self.setPrice("EUR 645.00"))
        print(self.setPrice(" US $762.52"))