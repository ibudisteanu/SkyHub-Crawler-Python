from Crawler.Objects.ObjectLink import ObjectLink
from Crawler.Objects.Products.ObjectProduct import ObjectProduct
from Crawler.Objects.Products.ObjectProductShipping import ObjectProductShipping
from Crawler.Objects.Products.ObjectReview import ObjectReview
from Crawler.Objects.Products.ObjectAuthor import ObjectAuthor

from Crawler.Helpers.LinksHelper import LinksHelper

#import urllib.parse
#import os.path
from pathlib import Path
import pickle
import requests  # Tutorial based on http://docs.python-requests.org/en/master/user/advanced/

fileLinksObjects = None
fileLinksVisited = None

arrLinksObjects = []
arrLinksVisited = []

class LinksDB():

    def __init__(self):
        pass

    @staticmethod
    def readLinksFiles(website):

        print("READING LINKS FILES for: ", website)

        global fileLinksObjects, fileLinksVisited
        global arrLinksObjects, arrLinksVisited

        filename = "data//link-objects//"+website+".xyz"
        if Path(filename).is_file():
            fileLinksObjects = open(filename, "rb")

            list = pickle.load(fileLinksObjects)

            arrLinksObjects.append({"website":website, list:list})

        filename = "data//urls-visited//" + website + ".xyz"
        if Path(filename).is_file():
            fileLinksVisited = open(filename, "r")

            content = fileLinksVisited.readlines()
            list = [x.strip() for x in content] # you may also want to remove whitespace characters like `\n` at the end of each line

            arrLinksVisited.append({"website":website, list:list})

    @staticmethod
    def appendLinksFiles(website):
        global arrLinksObjects, fileLinksVisited
        fileLinksVisited = open("data//urls_visited//"+website+".xyz", "a")

    @staticmethod
    def findLinkObjectAlready(website, url='', title='', allowTitleIncluded=False):
        url = LinksHelper.fix_url(url)

        global arrLinksObjects
        for object in arrLinksObjects:
            if (url == object.url) or (title == object.title):
                return object

            if allowTitleIncluded and (title in object.title or object.title in title):
                return object

        return None

    @staticmethod
    def checkLinkVisitedAlready(website, url):
        url = LinksHelper.fix_url(url)

        global arrLinksVisited
        if url in arrLinksVisited:
            return True
        return False

    @staticmethod
    def addLinkVisited(url):
        url = LinksHelper.fix_url(webiste, url)

        global arrLinksVisited
        global fileLinksVisited
        arrLinksVisited.append(url)
        fileLinksVisited.write(url)

    @staticmethod
    def addLinkObject(website, object):

        global arrLinksObjects
        global fileLinksObjects

        arrLinksObjects.append(object)

        fileLinksObjects = open("data//link_objects.xyz", "wb")
        pickle.dump(arrLinksObjects, fileLinksObjects, -1)
        fileLinksObjects.close()


