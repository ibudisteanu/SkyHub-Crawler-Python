print("Hello World!!")

import sys
sys.path.insert(0, 'Crawler')
sys.path.insert(0, 'Crawler/Crawlers')
sys.path.insert(0, 'Crawler/Helpers')
sys.path.insert(0, 'Server')


from Server.ServerAPI import ServerAPI

print(ServerAPI.getAddress("Ferdinand Street, No 28", "Romania"))

ServerAPI.loginUser("admin")
ServerAPI.loginUser("admin")
ServerAPI.loginUser("admin")
ServerAPI.postAddTopic("admin","","TITLU TEST","DESCRIERE","",["misto","coool","awesome"],[],"Romania","City","Romanian",-666,-666)


from scrapy.crawler import CrawlerProcess
from Crawler.Helpers.LinksHelper import LinksHelper

LinksHelper.readLinksFiles()
LinksHelper.appendLinksFiles()

from Crawler.Crawlers.CrawlerAntena3 import CrawlerAntena3
from Crawler.Crawlers.CrawlerAntena3Category import CrawlerAntena3Category

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(CrawlerAntena3)
process.crawl(CrawlerAntena3Category)
process.start() # the script will block here until the crawling is finished