from Crawler.Helpers.LinksHelper import LinksHelper

class ObjectReview:

    url = ''

    authorUsername = ''


    date = ''
    score = 5
    title = ''
    body = ''

    purchased = 0

    thumbsUp = 0
    thumbsDown = 0

    lastUpdate = 0

    def __init__(self, url, authorUsername, authorFullName, date, score, title, body, purchased, thumbsUp, thumbsDown,  lastUpdate=''):

        self.url = url
        self.url = LinksHelper.fix_url(self.url)

        self.authorUsername = authorUsername
        self.authorFullName = authorFullName
        self.date = date

        self.title = title
        self.body = body
        self.purchased = purchased
        self.thumbsUp = thumbsUp
        self.thumbsDown = thumbsDown

        self.score = score

        self.lastUpdate = lastUpdate

    def toString(self):

        if len(self.url) > 0: print("   url", self.url)
        if len(self.authorUsername) > 0: print("   username", self.authorUsername)
        if len(self.authorFullName) > 0: print("   fullname", self.authorFullName)
        if len(self.date) > 0: print("   date", self.date)
        if self.score > 0: print("   score", self.score)
        if len(self.title) > 0: print("   title", self.title)
        if len(self.body) > 0: print("   body", self.body)
        if len(self.purchased) > 0: print("   purchased", self.purchased)
        if self.thumbsUp > 0: print("   thumbsUp", self.thumbsUp)
        if self.thumbsDown > 0: print("   thumbsDown", self.thumbsDown)

        if len(self.lastUpdate) > 0: print("   lastUpdate", self.lastUpdate)