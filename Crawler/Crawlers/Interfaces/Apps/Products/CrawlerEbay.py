from Crawler.Crawlers.Interfaces.CrawlerProduct import CrawlerProduct

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
    websiteImage = "http://www.iconarchive.com/download/i31641/sykonist/popular-sites/eBay.ico"
    websiteCover = ""

    user = "muflonel2000"