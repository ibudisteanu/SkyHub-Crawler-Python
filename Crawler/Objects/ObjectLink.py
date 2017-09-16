from Crawler.Helpers.LinksHelper import LinksHelper

class ObjectLink:

    url = ''
    type = ''
    id = ''
    parent = ''
    title = ''

    def __init__(self, url, type, id, title, parent):

        self.url = url
        self.url = LinksHelper.fix_url(self.url)

        self.type = type
        self.id = id
        self.title = title
        self.parent = parent
