users = [
    {
        'username':'admin',
        'password': '',
        'id': '',
        'sessionId':'',
    },
    {
        'username': 'muflonel2000',
        'password': 'dsadas23123XXSD',
        'id': '',
        'sessionId': '',
    }
]

def getUser(username):
    for user in users:
        if (user['username'] == username) or (user['id'] == username):
            return user

    return None