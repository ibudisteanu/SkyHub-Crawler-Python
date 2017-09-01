from Crawler.Crawlers.CrawlerBlog import CrawlerBlog

class CrawlerFonduriUeRo(CrawlerBlog):

    name = 'CrawlerFonduriUeRo'

    url = 'http://www.fonduri-ue.ro'
    domain = 'fonduri-ue.ro'

    start_urls = (url,)
    allowed_domains = [domain]

    websiteCity = "Bucharest"
    websiteCountry = "Romania"
    websiteLanguage = "Romanian"
    websiteImage = "http://www.paginaeuropeana.ro/wp-content/uploads/2014/03/fonduri-europene-posdru.jpg"
    websiteCover = "http://ssub.ro/wp-content/uploads/2017/06/fonduristructurale21.jpg"

    user = "muflonel2000"