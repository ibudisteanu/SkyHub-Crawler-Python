import requests  # Tutorial based on http://docs.python-requests.org/en/master/user/advanced/

from Server.UsersTable import getUser

session = requests.Session()
userLoggedIn = None
url = "http://skyhub.me:4000/api/"
#url = "http://127.0.0.1:4000/api/"

class ServerAPI:
    def __init__(self):
        pass

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


    def postAddTopic(user, title, description, shortDescription,):
        user = ServerAPI.loginUser(user)

        if user == None:
            return False

        data = {
            'authorId': user['id'],
            'title': title,
            'description': description
        }

        headers = {}

        result = session.get(url + "auth/login", data=data, headers=headers)
        print(result)
        return result

    def postAddForum(user, name, title, description):
        user = ServerAPI.loginUser(user)

        if user == None:
            return False

        data = {
            'authorId': user['id'],
            'title': title,
            'name' : name,
            'description': description,
            'shortDescription' : shortDescription,
            'keywords': keywords,
            'country': country,
            'city': city,
            'latitude':
            'longtitude':

        dbLatitude = req.body.latitude | | -666;
        dbLongitude = req.body.longitude | | -666;

        sLanguage = req.body.language | | sCountry;

        sIconPic = req.body.iconPic | | '';
        sCoverPic = req.body.coverPic | | '';
        sCoverColor = req.body.coverColor | | '';
        parent = req.body.parent | | '';
            'title': title,
            'description': description
        }

        headers = {}

        result = session.get(url + "forums/add-forum", data=data, headers=headers)
        print(result)
        return result

    def getAddress(city, country):
        address = city + ' ' + country
        address = address.replace(' ', '+')

        session = requests.Session()
        result = session.get('https://maps.google.com/maps/api/geocode/json?address='+address+'&sensor=false')