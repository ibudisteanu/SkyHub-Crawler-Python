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

    feedbackRatings = []
    feedback2Ratings = []

    reviews = [] #reviews array of Review

    lastUpdate = 0

    def __init__(self,  url='', username='', userTitle='', id='', name='', score=0.0, feedbackOverall=0, feedbackRatings=[], feedback2Ratings=[], reviews=[], lastUpdate=0):

        self.url = url
        self.url = LinksHelper.fix_url(self.url)
        self.username = username

        self.userTitle = userTitle
        self.id = id
        self.name = name
        self.score = score
        self.feedbackOverall = feedbackOverall
        self.feedbackRatings = feedbackRatings
        self.feedback2Ratings = feedback2Ratings
        self.reviews = reviews
        self.lastUpdate = lastUpdate
