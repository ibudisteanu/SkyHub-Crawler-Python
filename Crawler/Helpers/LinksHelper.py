#import urllib.parse
#import os.path
from pathlib import Path
import pickle
import requests  # Tutorial based on http://docs.python-requests.org/en/master/user/advanced/

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
    def findLinkObjectAlready( url='', title='', allowTitleIncluded=False):
        url = LinksHelper.fix_url(url)

        global arrLinksObjects
        for object in arrLinksObjects:
            if (url == object.url) or (title == object.title):
                return object

            if allowTitleIncluded and (title in object.title or object.title in title):
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

    @staticmethod
    def fixArchiveStrings(text):

        # https://web.archive.org/web/20130502222444/
        if "web.archive.org/web/" in text:
            positionStart = text.index("web.archive.org/web/")
            text = text[positionStart + len("web.archive.org/web/20130502222444/"):10000]

        if "http" in text:
            positionStart = text.index("http")
            if positionStart != 0:
                text = text[positionStart:10000]

        return text



    @staticmethod
    def getRequestTrials(session, url,  data={}, headers={}, maxTrials = 5):
        error = True
        trials = 0
        while error == True and trials < maxTrials:
            error = False
            trials += 1
            try:
                response = session.get(url , data=data, headers=headers)
                if response.status_code == 503:
                    response.raise_for_status()
            except requests.exceptions.HTTPError as e:
                if e.response.status_code == 503:
                    error = True
                # handle your 503 specific error

        return response