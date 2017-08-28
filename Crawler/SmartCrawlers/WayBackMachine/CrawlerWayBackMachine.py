import dateparser
import requests  # Tutorial based on http://docs.python-requests.org/en/master/user/advanced/

from scrapy.crawler import CrawlerProcess
from Crawler.Helpers.LinksHelper import LinksHelper
from parsel import Selector

class CrawlerWayBackMachine:

    session = None
    process = None

    crawler = None

    def __init__(self):

        self.session = requests.Session()

        pass

    def start(self, crawler):

        crawler.onlyOnePage = True
        self.crawler = crawler

        self.getAllLinks(crawler.url)


    def getAllLinks(self, link):

        data = {}
        headers = {}

        url = "https://web.archive.org/cdx/search?url="+link+"%2F&matchType=prefix&collapse=urlkey&output=json&fl=original%2Cmimetype%2Ctimestamp%2Cendtimestamp%2Cgroupcount%2Cuniqcount&filter=!statuscode%3A%5B45%5D..&_=1503841753810"

        result = self.session.get(url, data=data, headers=headers)
        result = result.json()

        # Sample of answers from Archive.org
        # [["original", "mimetype", "timestamp", "endtimestamp", "groupcount", "uniqcount"],
        #  ["http://hackpedia.info:80/", "text/html", "20070820075302", "20110703091504", "301", "227"],
        #  ["http://hackpedia.info:80/bcprojects/?", "text/html", "20100708131643", "20100708150508", "3", "3"],
        #  ["http://hackpedia.info:80/bcprojects/index.php?", "text/html", "20100708131647", "20071201075458", "7", "6"],
        #  ["http://www.hackpedia.info:80/cpanel", "text/html", "20080907232733", "20090525064749", "15", "7"],

        index = 0
        for object in result:
            if index >= 1:
                url = object[0]
                mimetype = object[1]
                timestamp = object[2]
                endtimestamp = object[3]

                print(url, mimetype, timestamp, endtimestamp)

                if mimetype == "text/html":
                    self.processURL(url, timestamp, endtimestamp)

            index +=1

        return None

    def processURL(self, initialURL, timestamp, endtimestamp):
        # https://web.archive.org/web/20130502222444/http://hackpedia.info/viewtopic.php?f=43&t=16653&p=116862&sid=2a60dce4bac29bf5b399c5741f4e5cb3

        #initialURL = "http://hackpedia.info/viewtopic.php?f=14&t=14764&sid=97ffaea0727ec816f88a27e7a6778587"

        for rejection in self.crawler.rejectionSubstr:
            if rejection in initialURL:
                return None

        url = "https://web.archive.org/web/"+endtimestamp+"/"+initialURL

        data = {}
        headers = {}

        html = self.session.get(url , data=data, headers=headers)
        html = html.content
        html = html.decode("utf-8")
        #print(html)
        #print(type(html))

        sel = Selector(text=html)

        self.crawler.parseResponse(sel, initialURL)

        print("crawler parse done")
