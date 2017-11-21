import requests  # Tutorial based on http://docs.python-requests.org/en/master/user/advanced/

from Server.UsersTable import getUser
from Crawler.Helpers.LinksHelper import LinksHelper
import ujson

session = requests.Session()
userLoggedIn = None
#url = "http://skyhub.me:4000/api/"
url = "http://127.0.0.1:4000/api/"

class ServerAPI:
    def __init__(self):
        pass

    @staticmethod
    def logoutUser():

        print("Loggout user")

        data = {}
        headers = {}

        result = session.get(url+"auth/logout", data=data, headers=headers)
        result = result.json()
        print(result)
        if result['result'] == True:
            print("User Logged Out successfully ", result['result'])
            return True

        return False

    @staticmethod
    def loginUser(user):

        user = getUser(user)
        if user is None:
            return None

        global userLoggedIn
        if (userLoggedIn is not None):

            if (userLoggedIn['username'] == user['username'])or(userLoggedIn['id'] == user['id']):
                print("User Already logged in")
                return user
            else:
                ServerAPI.logoutUser()

        print("Loggin user")

        data = {
            'emailUsername': user['username'],
            'password': user['password']
        }

        headers = {}

        result = session.get(url+"auth/login", data=data, headers=headers)
        result = result.json()
        print(result)
        if result['result'] == True:
            print("User Logged In ", result['user']['id'])
            user['id'] = result['user']['id']
            user['sessionId'] = result['sessionId']
            userLoggedIn = user
            return user
        return None

    @staticmethod
    def postAddForum(rootURL, user, parentId, name, title, description, iconPic, coverPic, arrKeywords = [],  dtOriginalDate = None, country='', city='', language='',  latitude=-666, longitude=-666):

        user = ServerAPI.loginUser(user)

        if user is None: return False

        title = LinksHelper.fixArchiveStrings(title)
        description = LinksHelper.fixArchiveStrings(description)
        iconPic = LinksHelper.fixArchiveStrings(iconPic)
        coverPic = LinksHelper.fixArchiveStrings(coverPic)

        description = LinksHelper.fix_relative_urls(description, rootURL)

        rez = ServerAPI.processLocation(country, city, language, latitude, longitude)
        latitude = rez[0]
        longitude = rez[1]

        arrAdditionalInfo = {
            'scraped':True,
        }

        if dtOriginalDate is not None: arrAdditionalInfo['dtOriginal'] = dtOriginalDate

        if isinstance(arrKeywords, str): keywords = arrKeywords
        else: keywords = ','.join(str(e) for e in arrKeywords)

        data = {
            'id': user['id'],
            'sessionId': user['sessionId'],

            'parent': parentId,
            'title': title,
            'name': name,
            'description': description,
            'iconPic': iconPic,
            'coverPic': coverPic,
            'keywords': keywords,
            'country': country,
            'city': city,
            'language': language,
            'latitude': latitude,
            'longitude': longitude,
            'additionalInfo': ujson.dumps(arrAdditionalInfo)
        }

        headers = {}

        result = LinksHelper.getRequestTrials(session, url + "forums/add-forum", data, headers, maxTrials = 5)
        result = result.json()
        #print(result)
        if result['result'] == True:
            print('FORUM new ', result['forum']['URL'])
            return result['forum']['id']
        else:
            print("ERROR adding new forum ", result)
            return None

    @staticmethod
    def postAddTopic(rootURL, url, user, parentId, title, description, shortDescription='', arrKeywords=[], arrAttachments=[],
                     dtOriginalDate=None, country='', city='', language='', latitude=-666, longitude=-666,
                     authorName='', authorAvatar=''):
        user = ServerAPI.loginUser(user)

        if user is None: return False

        #print("######### DESCRIPTION ##############", description)

        title = LinksHelper.fixArchiveStrings(title)
        description = LinksHelper.fixArchiveStrings(description)
        shortDescription = LinksHelper.fixArchiveStrings(shortDescription)
        authorAvatar = LinksHelper.fixArchiveStrings(authorAvatar)
        authorName = LinksHelper.fixArchiveStrings(authorName)

        #print("######### DESCRIPTION 2 ##############", description)
        description = LinksHelper.fix_relative_urls(description, rootURL)

        #print("######### DESCRIPTION 3##############", description)
        rez = ServerAPI.processLocation(country, city, language, latitude, longitude)
        latitude = rez[0]
        longitude = rez[1]

        arrAdditionalInfo = {
            'scraped': True,
            'source': {
                'page': url,
                'website': rootURL,
            }
        }

        if dtOriginalDate is not None: arrAdditionalInfo['dtOriginal'] = dtOriginalDate
        if authorName != '': arrAdditionalInfo['orgName'] = authorName
        if authorAvatar != '': arrAdditionalInfo['orgAvatar'] = authorAvatar

        if isinstance(arrKeywords, str):
            keywords = arrKeywords
        else:
            keywords = ','.join(str(e) for e in arrKeywords)

        print("useR", user)

        data = {
            'id': user['id'],
            'sessionId': user['sessionId'],

            'parent': parentId,
            'title': title,
            'description': description,
            'shortDescription': shortDescription,
            'keywords': keywords,
            'attachments': ujson.dumps(arrAttachments),
            'country': country,
            'city': city,
            'language': language,
            'latitude': latitude,
            'longitude': longitude,
            'additionalInfo': ujson.dumps(arrAdditionalInfo)
        }

        headers = {}

        result = LinksHelper.getRequestTrials(session, url + "topics/add-topic", data, headers, maxTrials = 5)
        result = result.json()

        # print(result)
        if result['result'] == True:
            print('topic new ', result['topic']['URL'])
            return result['topic']['id']
        else:
            print("ERROR adding new topic ",result)
            return None

    @staticmethod
    def postAddProduct(rootURL, url, user, parentId, title, description, shortDescription='', arrKeywords=[], arrAttachments=[],
                       dtOriginalDate=None, country='', city='', language='', latitude=-666, longitude=-666,
                       itemId='', author=None, timeLeft=0, details=None, price=None, ratingScoresList=None, shipping=None, reviewsList=None, lastUpdate=''):

        user = ServerAPI.loginUser(user)

        if user is None: return False

        title = LinksHelper.fixArchiveStrings(title)
        description = LinksHelper.fixArchiveStrings(description)
        shortDescription = LinksHelper.fixArchiveStrings(shortDescription)
        authorAvatar = LinksHelper.fixArchiveStrings(author.avatar)
        authorName = LinksHelper.fixArchiveStrings(author.username)

        description = LinksHelper.fix_relative_urls(description, rootURL)

        rez = ServerAPI.processLocation(country, city, language, latitude, longitude)
        latitude = rez[0]
        longitude = rez[1]

        arrAdditionalInfo = {
            'scraped': True,
            'source': {
                'page': url,
                'website': rootURL,
            },

            'itemId': itemId,
            'timeLeft': timeLeft,
        }

        if dtOriginalDate is not None: arrAdditionalInfo['dtOriginal'] = dtOriginalDate
        if authorName != '': arrAdditionalInfo['orgName'] = authorName
        if authorAvatar != '': arrAdditionalInfo['orgAvatar'] = authorAvatar

        if isinstance(arrKeywords, str):
            keywords = arrKeywords
        else:
            keywords = ','.join(str(e) for e in arrKeywords)

        data = {
            'id': user['id'],
            'sessionId': user['sessionId'],

            'parent': parentId,
            'title': title,
            'description': description,
            'shortDescription': shortDescription,
            'keywords': keywords,
            'attachments': ujson.dumps(arrAttachments),
            'country': country,
            'city': city,
            'language': language,
            'latitude': latitude,
            'longitude': longitude,
            'additionalInfo': ujson.dumps(arrAdditionalInfo),

             # additional product information

            'author': ujson.dumps(author.getJSON()),
            'details': ujson.dumps(details.getJSON()),
            'price': ujson.dumps(price.getJSON()),
            'ratingScoresList': ujson.dumps(ratingScoresList.getJSON()),
            'shipping': ujson.dumps(shipping.getJSON()),
            'reviewsList': ujson.dumps(reviewsList.getJSON()),
            'lastUpdate': lastUpdate
        }

        headers = {}

        result = LinksHelper.getRequestTrials(session, url + "topics/add-topic", data, headers, maxTrials = 5)
        result = result.json()

        # print(result)
        if result['result'] == True:

            print('topic new ', result['topic']['URL'])
            return result['topic']['id']
        else:
            print("ERROR adding new topic ", result)
            return None

    @staticmethod
    def postAddReply(rootURL, user, parentId, parentReplyId, title, description, arrKeywords = [], arrAttachments=[], dtOriginalDate = None, country='', city='', language='',  latitude=-666, longitude=-666, authorName='', authorAvatar='' ):

        user = ServerAPI.loginUser(user)

        if user is None: return False
        if parentId is None: return False
        if parentReplyId is None: parentReplyId = ""

        title = LinksHelper.fixArchiveStrings(title)
        description = LinksHelper.fixArchiveStrings(description)
        authorAvatar = LinksHelper.fixArchiveStrings(authorAvatar)
        authorName = LinksHelper.fixArchiveStrings(authorName)

        description = LinksHelper.fix_relative_urls(description, rootURL)

        rez = ServerAPI.processLocation(country, city, language, latitude, longitude)
        latitude = rez[0]
        longitude = rez[1]

        arrAdditionalInfo = {
            'scraped':True,
        }

        if dtOriginalDate is not None: arrAdditionalInfo['dtOriginal'] = dtOriginalDate
        if authorName != '': arrAdditionalInfo['orgName'] = authorName
        if authorAvatar != '': arrAdditionalInfo['orgAvatar'] = authorAvatar

        if isinstance(arrKeywords, str): keywords = arrKeywords
        else: keywords = ','.join(str(e) for e in arrKeywords)

        data = {
            'id': user['id'],
            'sessionId': user['sessionId'],

            'parent': parentId,
            'parentReply': parentReplyId,
            'title': title,
            'description': description,
            'keywords': keywords,
            'attachments': ujson.dumps(arrAttachments),
            'country': country,
            'city': city,
            'language': language,
            'latitude': latitude,
            'longitude': longitude,
            'additionalInfo': ujson.dumps(arrAdditionalInfo)
        }

        headers = {}

        result = LinksHelper.getRequestTrials(session, url + "replies/add-reply", data, headers, maxTrials = 5)
        result = result.json()

        #print(result)
        if result['result'] == True:
            print('reply new ', result['reply']['URL'])
            return result['reply']['id']
        else:
            print("ERROR adding new reply ",result)
            return None

    @staticmethod
    def processLocation(country, city, language, latitude, longitude):
        if ((country or language) != '') or (city != ''):
            location = ServerAPI.getAddress(city, (country or language))
            if location is not None:
                latitude = location['lat']
                longitude = location['lng']

        return [latitude, longitude]

    @staticmethod
    def getAddress(city, country):
        address = city + ' ' + country
        address = address.replace(' ', '+')

        session = requests.Session()
        result = LinksHelper.getRequestTrials(session, 'https://maps.google.com/maps/api/geocode/json?address='+address+'&sensor=false', {}, {}, maxTrials=5)
        result = result.json()
        if len(result['results']) > 0:
            result =result['results'][0]['geometry']['location']
        else:
            result = None
        return result



