import dateparser

from Crawler.Crawlers.Interfaces.CrawlerNews import CrawlerNews


class CrawlerEvent(CrawlerNews):

    name = 'CrawlerBlog'

    url = 'http://fonduri-ue.ro'
    domain = 'fonduri-ue.ro'

    start_urls = (url,)
    allowed_domains = [domain]

    cssTitle = ""
    cssAuthor = ""
    cssAuthorLink = ""
    cssFullDescription = ""

    cssParent = ""

    cssOrganisation = ""
    cssLocation = ""
    cssHashTag = ""

    cssPrice = ""

    cssSpeakers = ""

    cssDateFrom = ""
    cssDateTo = ""

    cssTimeFrom = ""
    cssTimeTo = ""

    # variables

    removeShortDescription = True

    organisation = ''
    location = ''
    hashTag = ''

    price = ''

    dateFrom = ''
    dateTo = ''

    timeFrom = ''
    timeTo = ''

    def crawlerProcess(self, response, url):

        super().crawlerProcess(response, url)

        if self.cssOrganisation != '': self.organisation = self.extractFirstElement(response.css(self.cssOrganisation))

        if self.cssLocation != '': self.location = self.extractFirstElement(response.css(self.cssLocation))

        if self.cssDateFrom != '': self.dateFrom = self.extractFirstElement(response.css(self.cssDateFrom))

        if self.cssDateTo != '': self.dateTo = self.extractFirstElement(response.css(self.cssDateTo))

        if self.cssTimeFrom != '': self.timeFrom = self.extractFirstElement(response.css(self.cssTimeFrom))

        if self.cssTimeTo != '': self.timeTo = self.extractFirstElement(response.css(self.cssTimeTo))



    def validate(self):
        if (len(self.title) > 3) and (len(self.fullDescription) > 40) and len(self.cssLocation) > 2:
            return 'event'

        return ''

    def toString(self):

        super().toString()

        if self.organisation != '': print("organisation: ", self.organisation)
        if self.location != '': print("location: ", self.location)
        if self.hashTag != '': print("hashTag: ", self.hashTag)
        if self.price != '': print("price: ", self.price)
        if self.dateFrom != '': print("dateFrom: ", self.dateFrom)
        if self.dateTo != '': print("dateTo: ", self.dateTo)
        if self.timeFrom != '': print("timeFrom: ", self.timeFrom)
        if self.timeTo != '': print("timeTo: ", self.timeTo)

    def toJSON(self):

        json = super().toJSON()
        if self.organisation != '': json["organisation"] = self.organisation
        if self.location != '': json["location"] = self.location
        if self.hashTag != '': json["hashTag"] = self.hashTag
        if self.price != '': json["price"] = self.price
        if self.dateFrom != '': json["dateFrom"] = self.dateFrom
        if self.dateTo != '': json["dateTo"] = self.dateTo
        if self.timeFrom != '': json["timeFrom"] = self.timeFrom
        if self.timeTo != '': json["timeTo"] = self.timeTo
        return json