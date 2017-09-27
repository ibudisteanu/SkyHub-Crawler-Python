from Crawler.Helpers.LinksHelper import LinksHelper
from Crawler.Objects.Products.ObjectRatingScore import ObjectRatingScore

class ObjectRatingScoresList:

    ratingsList = []
    ratingsTotal = 0

    lastUpdate = 0

    def __init__(self, ratingsList=[], ratingsTotal=0, lastUpdate=''):

        self.ratingsList = ratingsList
        self.ratingsTotal = ratingsTotal

        self.lastUpdate = lastUpdate

    def toString(self):

        print("   Rating Scores List", len(self.ratingsList))
        if len(self.ratingsList) >0:
            for i, rating in enumerate(self.ratingsList):
                print("   Rating Scores List")
                rating.toString()

        print("   ratings total", self.ratingsTotal)

        if len(self.lastUpdate) > 0: print("   lastUpdate", self.lastUpdate)