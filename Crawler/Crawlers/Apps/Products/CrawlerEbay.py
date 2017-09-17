from Crawler.CrawlerBasic import CrawlerBasic
from Crawler.Crawlers.CrawlerProduct import CrawlerProduct

class CrawlerEbay(CrawlerProduct):

    name = 'CrawlerEbay'

    url = 'http://ebay.com'
    domain = 'ebay.com'

    start_urls = (url,)
    allowed_domains = [domain]

    websiteName = "Ebay"
    websiteCity = "Mountain View"
    websiteCountry = "USA"
    websiteLanguage = "English"
    websiteImage = ""
    websiteCover = ""

    user = "muflonel2000"