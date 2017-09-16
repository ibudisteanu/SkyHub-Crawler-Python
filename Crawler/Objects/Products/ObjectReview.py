from Crawler.Helpers.LinksHelper import LinksHelper

class ObjectReview:

    url = ''

    authorUsername = ''


    date = ''
    score = 5
    title = ''
    description = ''

    additionalInfo = ''

    thumbsUp = 0
    thumbsDown = 0

    lastUpdate = 0

    def __init__(self, url, authorUsername, date, score, title, description, additionalInfo, thumbsUp, thumbsDown, lastUpdate):

        self.url = url
        self.url = LinksHelper.fix_url(self.url)

        self.authorUsername = authorUsername
        self.date = date
        self.score = score
        self.title = title
        self.description = description
        self.additionalInfo = additionalInfo
        self.thumbsUp = thumbsUp
        self.thumbsDown = thumbsDown
        self.lastUpdate = lastUpdate
