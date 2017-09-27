from Crawler.Helpers.LinksHelper import LinksHelper
from Crawler.Objects.Products.ObjectRatingScore import ObjectRatingScore

class ObjectReviewsList:

    reviewsList = []

    lastUpdate = 0

    def __init__(self, reviewsList=[], lastUpdate=''):

        self.reviewsList = reviewsList

        self.lastUpdate = lastUpdate

    def toString(self):

        print("   Reviews List", len(self.reviewsList))
        if len(self.reviewsList) >0:
            for i, review in enumerate(self.reviewsList):
                print("   Review List")
                review.toString()

        if len(self.lastUpdate) > 0: print("   lastUpdate", self.lastUpdate)


    def getJSON(self):

        data = {
        }

        if len(self.reviewsList) > 0:
            list = []
            for i, review in enumerate(self.reviewsList):
                list.append(review.getJSON())

            data['reviewsList'] = list

        return data