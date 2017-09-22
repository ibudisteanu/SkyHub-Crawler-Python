from Crawler.Helpers.LinksHelper import LinksHelper

#import urllib.parse
#import os.path

from pathlib import Path
import pickle
import requests  # Tutorial based on http://docs.python-requests.org/en/master/user/advanced/

fileLinksObjects = None
fileLinksVisited = None

arrLinksObjects = {}
arrLinksVisited = {}

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

            arrLinksObjects[website] = list

        filename = "data//urls-visited//" + website + ".xyz"
        if Path(filename).is_file():
            fileLinksVisited = open(filename, "r")

            content = fileLinksVisited.readlines()
            list = [x.strip() for x in content] # you may also want to remove whitespace characters like `\n` at the end of each line

            arrLinksVisited[website] = list

    @staticmethod
    def findLinkObjectAlready(website, url='', title='', allowTitleIncluded=False):
        url = LinksHelper.fix_url(url)

        global arrLinksObjects

        if hasattr(arrLinksObjects, website) == False:
            return False

        list = arrLinksObjects[website]

        if list is not None:
            for object in list:
                if (url == object.url) or (title == object.title):
                    return object

                if allowTitleIncluded and (title in object.title or object.title in title):
                    return object

        return None

    @staticmethod
    def checkLinkVisitedAlready(website, url):
        url = LinksHelper.fix_url(url)

        global arrLinksVisited

        if hasattr(arrLinksVisited, website) == False:
            return False

        list = arrLinksVisited[website]
        if list is not None:
            if url in list:
                return True

        return False

    @staticmethod
    def addLinkVisited(website, url):
        url = LinksHelper.fix_url(url)

        if LinksDB.checkLinkVisitedAlready(website, url) == True:
            return False

        global arrLinksVisited
        global fileLinksVisited

        if hasattr(arrLinksVisited, website) == False:
            arrLinksVisited[website] = []

        arrLinksVisited[website].append(url)

        fileLinksVisited = open("data//urls_visited//"+website+".xyz", "wb")
        pickle.dump(arrLinksVisited[website], fileLinksVisited, -1)
        fileLinksVisited.close()


    @staticmethod
    def addLinkObject(website, object):

        global arrLinksObjects
        global fileLinksObjects

        if hasattr(arrLinksObjects, website) == False:
            arrLinksObjects[website] = []

        arrLinksObjects[website].append(object)

        fileLinksObjects = open("data//link_objects//"+website+".xyz", "wb")
        pickle.dump(arrLinksObjects[website], fileLinksObjects, -1)
        fileLinksObjects.close()


