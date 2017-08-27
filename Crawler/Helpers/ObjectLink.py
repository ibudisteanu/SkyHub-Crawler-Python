from Crawler.Helpers.LinksHelper import LinksHelper

class ObjectLink:

    url = ''
    type = ''
    id = ''
    parent = ''
    title = ''

    def __init__(self, url, type, id, text, parent):

        self.url = url
        self.url = LinksHelper.fix_url(self.url)

        self.type = type
        self.id = id
        self.text = text
        self.parent = parent
