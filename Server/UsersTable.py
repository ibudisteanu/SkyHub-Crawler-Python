users = [
    {
        'username':'admin',
        'password': '',
        'id': '2222',
    }
]

def getUser(username):
    for user in users:
        if (user['username'] == username) or (user['id'] == username):
            return user

    return None