#!/usr/bin/env python
print("Hello World!!")

import sys
sys.path.insert(0, 'Crawler')
sys.path.insert(0, 'Crawler/Crawlers')
sys.path.insert(0, 'Crawler/Crawlers/Apps')
sys.path.insert(0, 'Crawler/Helpers')
sys.path.insert(0, 'SmartCrawlers/WayBackMachine')
sys.path.insert(0, 'Server')

def CrawlerWayBackMachine():
    from Crawler.SmartCrawlers.WayBackMachine import CrawlerWayBackMachine
    crawlerWayBackMachine = CrawlerWayBackMachine.CrawlerWayBackMachine()

    from Crawler.Crawlers.Interfaces.Apps.CrawlerPHPBB import CrawlerPHPBB

    #hackpedia.info
    crawlerWayBackMachine.start(CrawlerPHPBB(user="muflonel2000", url="hackpedia.info", forumGrandParentId='1_forum_14996534590908914', websiteName='Hackpedia', websiteImage="https://a.wattpad.com/useravatar/anon_hacker.128.204872.jpg", websiteCover="https://www.cryptus.in/image/online-training-cceh.jpg", websiteCountry="Romania", websiteCity="Bucharest", websiteLanguage="Romanian"))

    #from Crawler.Crawlers.CrawlerTurkishajan import  CrawlerTurkishajan
    #crawlerWayBackMachine.start(CrawlerTurkishajan(user="muflonel2000", url="turkishajan.com", forumGrandParentId='1_forum_14996534590908914', websiteName='Turkishajan', websiteImage="https://pbs.twimg.com/profile_images/660874924815310848/ymph0vVr.jpg", websiteCover="https://www.technobezz.com/files/uploads/2016/01/Turkish-Hacker-Sentenced-To-344-years-1170x644.jpg", websiteCountry="Turkey", websiteCity="Instanbul", websiteLanguage="Turkish"))

    # from Crawler.Crawlers.CrawlerPHPBBForums import CrawlerPHPBBForums
    # crawlerWayBackMachine.start(CrawlerPHPBBForums, "hackpedia.info")




def testServerAPI():
    from Server.ServerAPI import ServerAPI
    print(ServerAPI.getAddress("Ferdinand Street, No 28", "Romania"))

    ServerAPI.loginUser("muflonel2000")
    ServerAPI.loginUser("muflonel2000")
    ServerAPI.loginUser("muflonel2000")
    topic = ServerAPI.postAddTopic("muflonel2000","","TITLU TEST77","DESCRIERE","",["misto","coool","awesome"],[],"2017-08-27T13:55:54+00:00","Romania","City","Romanian",-666,-666)
    #forum = ServerAPI.postAddForum("admin","","NAME - FORUM","NAME - FORUM TITLE","DESCRIERE","https://cdn4.iconfinder.com/data/icons/ionicons/512/icon-image-128.png","http://colorfully.eu/wp-content/uploads/2012/10/empty-road-highway-with-fog-facebook-cover.jpg",["misto","coool","awesome"]."2017-08-27T13:55:54+00:00","Romania","City","Romanian",-666,-666)
    #reply = ServerAPI.postAddReply("admin",topic,"","Reply5","DESCRIERE",["misto","coool","awesome"],[],"2017-08-27T13:55:54+00:00","Romania","City","Romanian",-666,-666)


def testProductPriceCurrency():

    from Crawler.Objects.Products.ObjectProductPrice import ObjectProductPrice
    price = ObjectProductPrice()
    price.testCurrencyConverter()


def CrawlerScrapy():
    from scrapy.crawler import CrawlerProcess

    scrapyProcess = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    # from Crawler.Crawlers.CrawlerAntena3 import CrawlerAntena3
    # scrapyProcess.crawl(CrawlerAntena3)
    #
    # from Crawler.Crawlers.CrawlerAntena3Category import CrawlerAntena3Category
    # scrapyProcess.crawl(CrawlerAntena3Category)

    # from Crawler.Crawlers.Apps.CrawlerFonduriUeRo import CrawlerFonduriUeRo
    # scrapyProcess.crawl(CrawlerFonduriUeRo)

    #from Crawler.Crawlers.Interfaces.Apps.Products.CrawlerEbay import  CrawlerEbay
    #scrapyProcess.crawl(CrawlerEbay)

    #from Crawler.Crawlers.Interfaces.Apps.Events.CrawlerNewAmericaOrg import CrawlerNewAmericaOrg
    #scrapyProcess.crawl(CrawlerNewAmericaOrg)

    from Crawler.Crawlers.Interfaces.Apps.Events.CrawlerCatoOrg import CrawlerCatoOrg
    scrapyProcess.crawl(CrawlerCatoOrg)

    scrapyProcess.start() # the script will block here until the crawling is finished

#init main


#CrawlerWayBackMachine()


CrawlerScrapy()

#testProductPriceCurrency()