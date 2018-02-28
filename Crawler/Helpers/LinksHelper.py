#import urllib.parse
#import os.path
from pathlib import Path
import pickle
import requests  # Tutorial based on http://docs.python-requests.org/en/master/user/advanced/

class LinksHelper():

    def __init__(self):
        pass

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
    def fix_relative_urls(text, rootURL):
        # src='/img' pr href="/"

        text = text.replace("src='/", "src='"+rootURL+'/')
        text = text.replace('src="/', 'src="'+rootURL+'/')

        text = text.replace("href='/", "href='"+rootURL+'/')
        text = text.replace('href="/', 'href="'+rootURL+'/')

        return text


    @staticmethod
    def fixArchiveStrings(text):
        hypertext_transfer_protocol = ['https://', 'http://', '']

        for item in hypertext_transfer_protocol:
            result = '{}web.archive.org/web/'.format(item)
            if result in text:
                start, end = text.index(result) + len('{}20130502222444/'.format(result)), 10000
                text = text[start:end]

        return text

    @staticmethod
    def getRequestTrials(session, url,  data={}, headers={}, maxTrials = 5):

        if session is None:
            session = requests.Session()

        error = True
        trials = 0
        response = None

        while (error == True) and (trials < maxTrials):
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
