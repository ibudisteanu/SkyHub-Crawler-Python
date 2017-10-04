from Crawler.Helpers.LinksHelper import LinksHelper

class ObjectAuthor:

    url = ''
    username = ''

    # objectId from SkyHub
    id = ''

    userTitle = ''

    name = ''
    score = 0.0
    feedbackOverall = 0
    feedbackSummaryList = []

    avatar = ''
    link = ''



    feedbackRatings = []

    reviews = [] #reviews array of Review

    lastUpdate = 0

    def __init__(self,  url='', username='', userTitle='', id='', name='', avatar='', link='', score=0.0, feedbackOverall=0, feedbackSummaryList=[], feedbackRatings=[], reviews=[], lastUpdate=0):

        self.url = url
        self.url = LinksHelper.fix_url(self.url)
        self.username = username

        self.userTitle = userTitle
        self.id = id
        self.name = name
        self.avatar = avatar
        self.link = link

        self.score = score

        self.feedbackOverall = feedbackOverall
        self.feedbackSummaryList = feedbackSummaryList

        self.feedbackRatings = feedbackRatings

        self.reviews = reviews
        self.lastUpdate = lastUpdate

    def toString(self):

        if len(self.url) > 0: print("   url", self.url)
        if len(self.username) > 0: print("   username", self.username)
        if len(self.userTitle) > 0: print("   userTitle", self.userTitle)
        if len(self.id) > 0: print("   id", self.id)
        if len(self.name) > 0: print("   name", self.name)
        if len(self.avatar) > 0: print("   avatar", self.avatar)
        if len(self.link) > 0: print("   link", self.link)

        if isinstance(self.score, str):
            if len(self.score) > 0: print("   score", self.score)
        else: print(self.score)

        if isinstance(self.feedbackOverall, str):
            if len(self.feedbackOverall) > 0: print("   feedbackOverall", self.feedbackOverall)
        else: print(self.feedbackOverall)


        if len(self.feedbackSummaryList) > 0: print("   feedbackSummaryList", self.feedbackSummaryList)
        if len(self.feedbackRatings) > 0: print("   feedbackRatings", self.feedbackRatings)
        if len(self.reviews) > 0: print("   reviews", self.reviews)
        if self.lastUpdate > 0: print("   lastUpdate", self.lastUpdate)


    def getJSON(self):

        return {
            'url': self.url,
            'username': self.username,
            'userTitle': self.userTitle,
            'id': self.id,
            'name': self.name,
            'avatar': self.avatar,
            'link': self.link,
            'score': self.score,
            'feedbackOverall': self.feedbackOverall,
            'feedbackSummaryList': self.feedbackSummaryList,
            'feedbackRatings': self.feedbackRatings,
            'reviews': self.reviews,
            'lastUpdate': self.lastUpdate,
        }