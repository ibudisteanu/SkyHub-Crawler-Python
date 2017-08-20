print("Hello World!!")

from scrapy.crawler import CrawlerProcess
from LinksHelper import  LinksHelper

LinksHelper.readLinksFiles()
LinksHelper.appendLinksFiles()

from CrawlerAntena3 import CrawlerAntena3
from CrawlerAntena3Category import CrawlerAntena3Category

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(CrawlerAntena3)
process.crawl(CrawlerAntena3Category)
process.start() # the script will block here until the crawling is finished