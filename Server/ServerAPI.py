import requests  # Tutorial based on http://docs.python-requests.org/en/master/user/advanced/

from Server.UsersTable import getUser

session = requests.Session()
userLoggedIn = None
url = "http://skyhub.me:4000/api/"
#url = "http://127.0.0.1:4000/api/"

class ServerAPI:
    def __init__(self):
        pass

    @staticmethod
    def loginUser(user):

        user = getUser(user)
        if user == None:
            return False

        global userLoggedIn
        if (userLoggedIn != None) and ((userLoggedIn['username'] == user['username'])or(userLoggedIn['id'] == user['id'])):
            return userLoggedIn

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
            userLoggedIn = user
            return user
        return None

    @staticmethod
    def postAddTopic(user, parentId, title, description, shortDescription='',  arrKeywords=[], arrAttachments=[], country='', city='', language='' ):
        user = ServerAPI.loginUser(user)

        if user == None:
            return False

        data = {
            'authorId': user['id'],
            'parentId': parentId,
            'title': title,
            'description': description,
            'shortDescription': shortDescription,
            'keywords': arrKeywords,
            'attachments': arrAttachments,
            'country': country,
            'city': city,
            'language': language
        }

        headers = {}

        result = session.get(url + "auth/login", data=data, headers=headers)
        print(result)
        return result

    @staticmethod
    def postAddForum(user, parentId, name, title, description, iconPic, coverPic, arrKeywords = [], country='', city='', language=''):

        user = ServerAPI.loginUser(user)

        if user == None:
            return False

        data = {
            'authorId': user['id'],
            'parentId': parentId,
            'title': title,
            'name' : name,
            'description': description,
            'keywords': arrKeywords,
            'country': country,
            'city': city,
            'language': language,
        }

        headers = {}

        result = session.get(url + "forums/add-forum", data=data, headers=headers)
        print(result)
        return result

    @staticmethod
    def getAddress(city, country):
        address = city + ' ' + country
        address = address.replace(' ', '+')

        session = requests.Session()
        result = session.get('https://maps.google.com/maps/api/geocode/json?address='+address+'&sensor=false')
        result = result.json()
        if len(result['results']) > 0:
            result =result['results'][0]['geometry']['location']
        else:
            result = None
        return result