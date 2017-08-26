class AttrDict(dict): #according to https://stackoverflow.com/questions/2640806/javascript-like-object-in-python-standard-library
    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)
        self.__dict__ = self