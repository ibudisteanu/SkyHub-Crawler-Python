from Crawler.Crawlers.Interfaces.Apps.CrawlerEvent import CrawlerEvent

class CrawlerCatoOrg(CrawlerEvent):

    name = 'CrawlerCato'

    url = 'http://cato.org'
    domain = 'cato.org'

    start_urls = (url,)
    allowed_domains = [domain]

    saveJSONFile = True

    websiteCity = "Washington DC"
    websiteCountry = "USA"
    websiteLanguage = "English"
    websiteImage = ""
    websiteCover = ""

    user = "muflonel2000"

    cssDateFrom = "span.date-display-start ::attr(content)"
    cssTimeFrom = "span.date-display-end ::attr(content)"

    cssLocation = "div.body-text div.field-venue::text"
    cssLocationAddress = ""
    cssLocationCity = ""
    cssLocationState = ""

    cssSpeakers = "div.field-speakers ::text"

    cssFullDescription = "div.field-body"

    def validate(self):
        if (len(self.title) > 3) and (len(self.fullDescription) > 40) and len(self.location) > 2:

            if isinstance(self.speakers, str):
                self.speakers =  [x.strip() for x in self.speakers.split(',')]

            return 'event'

        return ''