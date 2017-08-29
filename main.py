#!/usr/bin/env python
print("Hello World!!")

import sys
sys.path.insert(0, 'Crawler')
sys.path.insert(0, 'Crawler/Crawlers')
sys.path.insert(0, 'Crawler/Helpers')
sys.path.insert(0, 'SmartCrawlers/WayBackMachine')
sys.path.insert(0, 'Server')

def CrawlerWayBackMachine():
    from Crawler.SmartCrawlers.WayBackMachine import CrawlerWayBackMachine
    crawlerWayBackMachine = CrawlerWayBackMachine.CrawlerWayBackMachine()

    from Crawler.Crawlers.CrawlerPHPBB import CrawlerPHPBBTopic
    crawlerWayBackMachine.start(CrawlerPHPBBTopic(user="muflonel2000", url="hackpedia.info", websiteName='Hackpedia', websiteImage="https://pbs.twimg.com/profile_images/660874924815310848/ymph0vVr.jpg", websiteCover="https://www.cryptus.in/image/online-training-cceh.jpg", websiteCountry="Romania", websiteCity="Bucharest", websiteLanguage="Romanian"))

    # from Crawler.Crawlers.CrawlerPHPBBForums import CrawlerPHPBBForums
    # crawlerWayBackMachine.start(CrawlerPHPBBForums, "hackpedia.info")




def testServerAPI():
    from Server.ServerAPI import ServerAPI
    print(ServerAPI.getAddress("Ferdinand Street, No 28", "Romania"))

    ServerAPI.loginUser("admin")
    ServerAPI.loginUser("admin")
    ServerAPI.loginUser("admin")
    #topic = ServerAPI.postAddTopic("admin","","TITLU TEST5","DESCRIERE","",["misto","coool","awesome"],[],"2017-08-27T13:55:54+00:00","Romania","City","Romanian",-666,-666)
    #forum = ServerAPI.postAddForum("admin","","NAME - FORUM","NAME - FORUM TITLE","DESCRIERE","https://cdn4.iconfinder.com/data/icons/ionicons/512/icon-image-128.png","http://colorfully.eu/wp-content/uploads/2012/10/empty-road-highway-with-fog-facebook-cover.jpg",["misto","coool","awesome"]."2017-08-27T13:55:54+00:00","Romania","City","Romanian",-666,-666)
    #reply = ServerAPI.postAddReply("admin",topic,"","Reply5","DESCRIERE",["misto","coool","awesome"],[],"2017-08-27T13:55:54+00:00","Romania","City","Romanian",-666,-666)





def CrawlerScrapy():
    from scrapy.crawler import CrawlerProcess

    from Crawler.Crawlers.CrawlerAntena3 import CrawlerAntena3
    from Crawler.Crawlers.CrawlerAntena3Category import CrawlerAntena3Category

    scrapyProcess = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    scrapyProcess.crawl(CrawlerAntena3)
    scrapyProcess.crawl(CrawlerAntena3Category)
    scrapyProcess.start() # the script will block here until the crawling is finished

#init main
from Crawler.Helpers.LinksHelper import LinksHelper
LinksHelper.readLinksFiles()
LinksHelper.appendLinksFiles()

CrawlerWayBackMachine()
CrawlerScrapy()