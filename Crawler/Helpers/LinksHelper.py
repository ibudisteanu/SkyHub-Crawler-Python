#import urllib.parse
#import os.path
from pathlib import Path

fileLinksProcessed = None
fileLinksVisited = None

arrLinksProcessed = []
arrLinksVisited = []

class LinksHelper():

    def __init__(self):
        self.readLinksFiles()
        self.appendLinksFiles()

    @staticmethod
    def readLinksFiles():

        print("READING LINKS FILES")

        global fileLinksProcessed, fileLinksVisited
        global arrLinksProcessed, arrLinksVisited

        if Path("data/urls_processed.xyz").is_file():
            fileLinksProcessed = open("data//urls_processed.xyz", "r")
            content = fileLinksProcessed.readlines()
            arrLinksProcessed = [x.strip() for x in content] # you may also want to remove whitespace characters like `\n` at the end of each line

        if Path("data/urls_visited.xyz").is_file():
            fileLinksVisited = open("data//urls_visited.xyz", "r")
            content = fileLinksVisited.readlines()
            arrLinksVisited = [x.strip() for x in content] # you may also want to remove whitespace characters like `\n` at the end of each line

    @staticmethod
    def appendLinksFiles():
        global fileLinksProcessed, fileLinksVisited
        fileLinksProcessed = open("data//urls_processed.xyz", "a")
        fileLinksVisited = open("data//urls_visited.xyz", "a")

    @staticmethod
    def checkLinkProcessedAlready( url):
        url = LinksHelper.fix_url(url)

        global arrLinksProcessed, arrLinksVisited
        if url in arrLinksProcessed:
            return True
        return False

    @staticmethod
    def checkLinkVisitedAlready(url):
        url = LinksHelper.fix_url(url)

        global arrLinksProcessed, arrLinksVisited
        if url in arrLinksProcessed:
            return True
        return False

    @staticmethod
    def addLinkVisited(url):
        url = LinksHelper.fix_url(url)

        global arrLinksVisited
        global fileLinksVisited
        arrLinksVisited.append(url)
        fileLinksVisited.write(url)

    @staticmethod
    def addLinkProcessed(url):
        url = LinksHelper.fix_url(url)

        global arrLinksProcessed
        global fileLinksProcessed
        arrLinksProcessed.append(url)
        fileLinksProcessed.write(url)

    @staticmethod
    def fix_url(url):   # based on https://stackoverflow.com/questions/32178535/repair-url-using-python
        url = url.lower()

        if url.find("https") >= 0:
            url = url.replace("https", "http")

        if url.find("http") < 0:
            url.replace("://", "")
            url = "http://"+url

        if (url.find("www.") >= 0) and (url.find("www.") < 10):
            url = url.replace("www.", "")

        return url