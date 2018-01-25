from Crawler.Crawlers.Interfaces.Apps.CrawlerBlog import CrawlerBlog

class CrawlerFonduriUeRo(CrawlerBlog):

    name = 'CrawlerFonduriUeRo'

    url = 'https://www.fonduri-ue.ro'
    domain = 'fonduri-ue.ro'

    start_urls = (url,)
    allowed_domains = [domain]

    websiteName = "Fonduri Europene UE"
    websiteCity = "Bucharest"
    websiteCountry = "Romania"
    websiteLanguage = "Romanian"
    websiteImage = "http://media.startupcafe.ro/sites/default/files/styles/200x200/public/image-2015-06-19-20243968-47-fonduri-europene-2017.jpg?itok=-BVj0cnU"
    websiteCover = "http://ssub.ro/wp-content/uploads/2017/06/fonduristructurale21.jpg"

    user = "muflonel2000"