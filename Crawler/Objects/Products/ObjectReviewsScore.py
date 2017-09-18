from Crawler.Helpers.LinksHelper import LinksHelper

class ObjectReviewScore:

    score = 0
    value = 0

    lastUpdate = 0

    def __init__(self, score, value, lastUpdate=''):
        self.score = score
        self.value = value
        self.lastUpdate = lastUpdate
