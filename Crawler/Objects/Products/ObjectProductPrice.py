from Crawler.Helpers.LinksHelper import LinksHelper

class ObjectProduct:

    listPrice = ''
    youSave = ''

    price = 0
    currency = ''

    lastUpdate = 0

    def __init__(self, listPrice, youSave, price, currency, lastUpdate ):

        self.listPrice = listPrice
        self.youSave = youSave
        self.price = price
        self.currency = currency
        self.lastUpdate = lastUpdate