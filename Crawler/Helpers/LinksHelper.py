#import urllib.parse
#import os.path
from pathlib import Path
import pickle

fileLinksObjects = None
fileLinksVisited = None

arrLinksObjects = []
arrLinksVisited = []

class LinksHelper():

    def __init__(self):
        self.readLinksFiles()
        self.appendLinksFiles()

    @staticmethod
    def readLinksFiles():

        print("READING LINKS FILES")

        global fileLinksObjects, fileLinksVisited
        global arrLinksObjects, arrLinksVisited

        if Path("data/link_objects.xyz").is_file():
            fileLinksObjects = open("data//link_objects.xyz", "rb")
            arrLinksObjects = pickle.load(fileLinksObjects)

        if Path("data/urls_visited.xyz").is_file():
            fileLinksVisited = open("data//urls_visited.xyz", "r")
            content = fileLinksVisited.readlines()
            arrLinksVisited = [x.strip() for x in content] # you may also want to remove whitespace characters like `\n` at the end of each line

    @staticmethod
    def appendLinksFiles():
        global arrLinksObjects, fileLinksVisited
        fileLinksVisited = open("data//urls_visited.xyz", "a")

    @staticmethod
    def findLinkObjectAlready( url='', title=''):
        url = LinksHelper.fix_url(url)

        global arrLinksObjects
        for object in arrLinksObjects:
            if (url == object.url) or (title == object.title):
                return object

        return None

    @staticmethod
    def checkLinkVisitedAlready(url):
        url = LinksHelper.fix_url(url)

        global arrLinksVisited
        if url in arrLinksVisited:
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
    def addLinkObject(object):

        global arrLinksObjects
        global fileLinksObjects

        arrLinksObjects.append(object)

        fileLinksObjects = open("data//link_objects.xyz", "wb")
        pickle.dump(arrLinksObjects, fileLinksObjects, -1)
        fileLinksObjects.close()

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

        url = url.split("#", 1)[0]

        return url