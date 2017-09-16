from Crawler.CrawlerProcess import CrawlerProcess

class CrawlerPHPBB(CrawlerProcess):

    name = 'CrawlerPHPForums'

    url = 'http://antena3.ro'
    domain = 'antena3.ro'
    rejectionSubstr =  ["/memberlist.php?","/posting.php?","/search.php?","/ucp.php?","/cron.php?","/help-others/","/parteneri/"]

    start_urls = (url,)
    allowed_domains = [domain]

    removeLastMessage = True

    #CSS
    bodyFilterCSS = "#pagecontent"

    cssTitle = "#pageheader > h2 > a::text"
    cssReplies = "div.postbody"
    cssAuthors = "div.postauthor"
    cssDates = "td.postbottom"
    cssAvatars = "div.postavatar img"
    cssTitles = "div.postsubject"

    cssBreadcrumbs = ''
    cssBreadcrumbsChildren = 'p.breadcrumbs > a'

    rejectReplyTitle = True

    def crawlerProcess(self, response, url):

        self.title = self.extractFirstElement(response.css(self.cssTitle))
        self.fullDescription = ''
        self.shortDescription = ''


        self.replies = []

        if self.bodyFilterCSS != '':
            response = response.css(self.bodyFilterCSS)

        replies = response.css(self.cssReplies)
        authors = response.css(self.cssAuthors)
        dates = response.css(self.cssDates)
        avatars = response.css(self.cssAvatars)
        titles = response.css(self.cssTitles)

        if len(replies) == len(authors)+1:
            if self.removeLastMessage: del replies[-1]

        if len(replies) > 0 and len(authors) > 0 and len(dates) > 0 and len(titles) > 0:
            for i, reply in enumerate(replies):
                reply = replies[i]
                reply = '<br/>'.join(reply.extract())

                if i < len(authors):
                    author = authors[i]
                    author = ' '.join(author.css("::text").extract())
                else: author = ''

                if i < len(dates):
                    if len(dates) == 2 * len(replies): date = dates[2*i]
                    else: date = dates[i]

                    date = ' '.join(date.css('::text').extract())

                if i < len(avatars):
                    avatar = avatars[i]
                    avatar = avatar.css('::attr(src)').extract_first()
                else: avatar = ''

                if i < len(titles):
                    title = titles[i]
                    title = ' '.join(title.css('::text').extract())
                else: title = ''


                if i == 0:
                    self.fullDescription = reply
                    self.shortDescription = ''
                    self.author = author
                    self.date = date
                    self.authorAvatar = avatar
                    #self.title = title
                else:
                    if self.rejectReplyTitle:
                        title = ''
                    self.replies.append({'description': reply, 'title':title, 'author':author, 'date':date, 'authorAvatar': avatar })

        self.parents = []

        if len(self.title) > 0:
            for i in reversed(range(1, 100)):
                parent = response.css(self.cssBreadcrumbsChildren+':nth-child('+str(i)+')')
                parentText = self.extractFirstElement(parent.css('::text'))
                parentURL = self.extractFirstElement(parent.css('::attr(href)'))

                if parentText != '':
                    self.parents.append({'name':parentText, 'url':parentURL, 'index': i})


        self.parents = list(reversed(self.parents)) #changing the order



    def validate(self):
        if len(self.title) > 0 and len(self.fullDescription) > 0:
            return 'topic'

        return ''