from Crawler.Helpers.LinksHelper import LinksHelper

from pathlib import Path
import pickle
import json

arrJSONObjects = {}

class JSONDB():

    def __init__(self):
        pass

    @staticmethod
    def readJSONObjectsFiles(website):

        print("READING LINKS FILES for: ", website)

        global arrJSONObjects

        filename = "data//JSON//"+website+".json"
        print("filename", filename)
        if Path(filename).is_file():
            file = open(filename, "rb")

            list = json.load(file)

            arrJSONObjects[website] = list

            print("FILE READ IT WORKS", list)
            return True

        return False



    @staticmethod
    def findLJSONObjectAlready(website, url='', title='', description='', allowTitleIncluded=False):
        url = LinksHelper.fix_url(url)

        global arrJSONObjects

        if (website in arrJSONObjects) == False:
            if JSONDB.readJSONObjectsFiles(website) == False:
                print("IT DOESNT WORK....")
                return None

        list = arrJSONObjects[website]

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
    def addJSONObject(website, object):

        global arrJSONObjects

        if (website in arrJSONObjects) == False:
            if JSONDB.readJSONObjectsFiles(website) == False:
                arrJSONObjects[website] = []

        arrJSONObjects[website].append(object)



    @staticmethod
    def saveJSONObjects():

        global arrJSONObjects

        for domain in arrJSONObjects:
            file = open("data//JSON//"+domain+".JSON", "w")
            json.dump(arrJSONObjects[domain], file)
            file.close()


def closeFiles():
    print("S-a TERMINAT JSON !!!")
    JSONDB.saveJSONObjects()

import atexit
atexit.register(closeFiles)