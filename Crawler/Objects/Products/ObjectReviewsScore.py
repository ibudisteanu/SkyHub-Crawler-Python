from Crawler.Helpers.LinksHelper import LinksHelper

class ObjectReviewScore:

    score = 0
    value = 0

    lastUpdate = 0

    def __init__(self, score, value, lastUpdate=''):
        self.score = score
        self.value = value
        self.lastUpdate = lastUpdate

    def toString(self):

        if len(self.score) > 0: print("   score", self.score)
        if len(self.value) > 0: print("   value", self.value)
        if len(self.lastUpdate) > 0: print("   lastUpdate", self.lastUpdate)