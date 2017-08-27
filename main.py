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
topic = ServerAPI.postAddTopic("admin","","TITLU TEST5","DESCRIERE","",["misto","coool","awesome"],[],"2017-08-27T13:55:54+00:00","Romania","City","Romanian",-666,-666)
#forum = ServerAPI.postAddForum("admin","","NAME - FORUM","NAME - FORUM TITLE","DESCRIERE","https://cdn4.iconfinder.com/data/icons/ionicons/512/icon-image-128.png","http://colorfully.eu/wp-content/uploads/2012/10/empty-road-highway-with-fog-facebook-cover.jpg",["misto","coool","awesome"]."2017-08-27T13:55:54+00:00","Romania","City","Romanian",-666,-666)
reply = ServerAPI.postAddReply("admin",topic,"","Reply5","DESCRIERE",["misto","coool","awesome"],[],"2017-08-27T13:55:54+00:00","Romania","City","Romanian",-666,-666)


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