from Crawler.Helpers.LinksHelper import LinksHelper

from pathlib import Path
import pickle

arrLinksObjects = {}
arrLinksVisited = {}

class LinksDB():

    def __init__(self):
        pass

    @staticmethod
    def readLinkObjectsFiles(website):

        print("READING LINKS FILES for: ", website)

        global arrLinksObjects

        filename = "data//link_objects//"+website+".xyz"
        print("filename", filename)
        if Path(filename).is_file():
            file = open(filename, "rb")

            list = pickle.load(file)

            arrLinksObjects[website] = list

            print("FILE READ IT WORKS", list)
            return True

        return False


    @staticmethod
    def readLinksVisitedFiles(website):

        print("READING LINKS FILES for: ", website)

        global arrLinksVisited

        filename = "data//urls_visited//" + website + ".xyz"
        if Path(filename).is_file():
            fileLinksVisited = open(filename, "rb")

            content = fileLinksVisited.readlines()
            #content = fileLinksVisited.read()
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
            for object in list:

                print(list)
                print("findObject", object, hasattr(object, 'title'))
                print( object.title, title, title == object.title)

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

        if (website in arrLinksVisited) == False:
            if LinksDB.readLinksVisitedFiles(website) == False:
                arrLinksVisited[website] = []

        arrLinksVisited[website].append(url)


    @staticmethod
    def addLinkObject(website, object):

        global arrLinksObjects;

        if (website in arrLinksObjects) == False:
            if LinksDB.readLinkObjectsFiles(website) == False:
                arrLinksObjects[website] = []

        arrLinksObjects[website].append(object)



    @staticmethod
    def saveLinkObjects():

        global arrLinksObjects

        for domain in arrLinksObjects:
            file = open("data//link_objects//"+domain+".xyz", "wb")
            pickle.dump(arrLinksObjects[domain], file, -1)
            file.close()

    @staticmethod
    def saveLinkVisited():

        global arrLinksVisited

        for domain in arrLinksVisited:
            file = open("data//urls_visited//"+domain+".xyz", "wb")
            pickle.dump(arrLinksVisited[domain], file, -1)
            file.close()

def closeFiles():
    print("S-a TERMINAT!!!")
    LinksDB.saveLinkObjects()
    LinksDB.saveLinkVisited()

import atexit
atexit.register(closeFiles)