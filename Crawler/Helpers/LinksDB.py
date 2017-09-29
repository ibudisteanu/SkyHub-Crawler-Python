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
    def readLinkObjectsFiles(website):

        print("READING LINKS FILES for: ", website)

        global fileLinksObjects
        global arrLinksObjects

        filename = "data//link-objects//"+website+".xyz"
        if Path(filename).is_file():
            fileLinksObjects = open(filename, "rb")

            list = pickle.load(fileLinksObjects)

            arrLinksObjects[website] = list
            return True

        return False


    @staticmethod
    def readLinksVisitedFiles(website):

        print("READING LINKS FILES for: ", website)

        global fileLinksVisited
        global arrLinksVisited

        filename = "data//urls-visited//" + website + ".xyz"
        if Path(filename).is_file():
            fileLinksVisited = open(filename, "r")

            content = fileLinksVisited.readlines()
            list = [x.strip() for x in
                    content]  # you may also want to remove whitespace characters like `\n` at the end of each line

            arrLinksVisited[website] = list
            return True

        return False



    @staticmethod
    def findLinkObjectAlready(website, url='', title='', description='', allowTitleIncluded=False):
        url = LinksHelper.fix_url(url)

        global arrLinksObjects

        if (website in arrLinksObjects) == False:
            if LinksDB.readLinkObjectsFiles(website) == False:
                print("IT DOESNT WORK....")
                return None

        list = arrLinksObjects[website]

        if list is not None:
            for object in enumerate(list):

                if ((hasattr(object, 'url'))and(url == object.url)) or \
                   ((title != '') and (hasattr(object, 'title')) and (title == object.title)) or \
                   ((description != '') and (hasattr(object, 'description')) and (description == object.description)):
                    return object

                if allowTitleIncluded and (title in object.title or object.title in title):
                    return object

        return None

    @staticmethod
    def checkLinkVisitedAlready(website, url):
        url = LinksHelper.fix_url(url)

        global arrLinksVisited

        if (website in arrLinksVisited) == False:
            if LinksDB.readLinksVisitedFiles(website) == False:
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

        if (website in arrLinksVisited) == False:
            if LinksDB.readLinksVisitedFiles(website) == False:
                arrLinksVisited[website] = []

        arrLinksVisited[website].append(url)

        fileLinksVisited = open("data//urls_visited//"+website+".xyz", "wb")
        pickle.dump(arrLinksVisited[website], fileLinksVisited, -1)
        fileLinksVisited.close()


    @staticmethod
    def addLinkObject(website, object):

        global arrLinksObjects
        global fileLinksObjects

        if (website in arrLinksObjects) == False:
            if LinksDB.readLinkObjectsFiles(website) == False:
                arrLinksObjects[website] = []

        arrLinksObjects[website].append(object)

        fileLinksObjects = open("data//link_objects//"+website+".xyz", "wb")
        pickle.dump(arrLinksObjects[website], fileLinksObjects, -1)
        fileLinksObjects.close()


