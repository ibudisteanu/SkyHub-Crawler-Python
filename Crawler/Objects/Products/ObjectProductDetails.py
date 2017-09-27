from Crawler.Helpers.LinksHelper import LinksHelper

class ObjectProductDetails:

    itemCondition = ''
    itemSpecifications = ''
    itemConditionDetails = ''
    itemBrand = ''
    itemMaterial = ''

    lastUpdate = 0

    def __init__(self, itemCondition='', itemSpecifications='', itemConditionDetails='', itemBrand='', itemMaterial='', lastUpdate='' ):

        self.itemCondition = itemCondition
        self.itemSpecifications = itemSpecifications
        self.itemConditionDetails = itemConditionDetails
        self.itemBrand = itemBrand
        self.itemMaterial = itemMaterial
        self.lastUpdate = lastUpdate


    def toString(self):

        if len(self.itemCondition) > 0: print("   Item Condition", self.itemCondition)
        if len(self.itemSpecifications) > 0: print("   Item Specifications", self.itemSpecifications)
        if len(self.itemConditionDetails) > 0: print("   Item Condition Details", self.itemConditionDetails)
        if len(self.itemBrand) > 0: print("   Item Brand", self.itemBrand)
        if len(self.itemMaterial) > 0: print("   Item Material", self.itemMaterial)

    def getJSON(self):

        return {
            'itemCondition': self.itemCondition,
            'itemSpecifications': self.itemSpecifications,
            'itemConditionDetails': self.itemConditionDetails,
            'itemBrand': self.itemBrand,
            'itemMaterial': self.itemMaterial,
        }