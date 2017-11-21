from Crawler.Crawlers.Interfaces.Apps.CrawlerEvent import CrawlerEvent

class CrawlerNewAmericaOrg(CrawlerEvent):

    name = 'CrawlerNewAmericaOrg'

    url = 'http://newamerica.org'
    domain = 'newamerica.org'

    start_urls = (url,)
    allowed_domains = [domain]

    saveJSONFile = True

    websiteCity = "Washington DC"
    websiteCountry = "USA"
    websiteLanguage = "English"
    websiteImage = ""
    websiteCover = ""

    user = "muflonel2000"

    cssDateFrom = "p.date::text"
    cssTimeFrom = "p.time::text"

    cssLocation = "div.event__right p::text"
    cssLocationAddress = "div.event__right p:first-child::text"
    cssLocationCity = "div.event__right p:last-child::text"
    cssLocationState = "div.event__right p:last-child::text"

    cssFullDescription = "div.post-body"