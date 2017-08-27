from Crawler.CrawlerBasic import CrawlerBasic

class CrawlerPHPBBTopic(CrawlerBasic):

    name = 'CrawlerPHPForums'

    url = 'http://antena3.ro'
    domain = 'antena3.ro'
    rejectionSubstr =  ["/memberlist.php?","/posting.php?","/search.php?","/ucp.php?","/cron.php?","/help-others/index.php?"]

    start_urls = (url,)
    allowed_domains = [domain]

    removeLastMessage = True

    def crawlerProcess(self, response, url):

        self.title = self.extractFirstElement(response.css('#pageheader > h2 > a::text'))

        self.replies = []

        response = response.css("#pagecontent")

        replies = response.css("div.postbody")
        if self.removeLastMessage: del replies[-1]
        for i, reply in enumerate(replies):
            reply = '<br/>'.join(reply.css("::text").extract())
            if i == 0:
                self.fullDescription = reply
                self.shortDescription = ''
            else:
                self.replies.append({'description': reply})


        authors = response.css("div.postauthor")
        if self.removeLastMessage: del authors[-1]
        for i, author in enumerate(authors):
            author = ' '.join(author.css("::text").extract())
            if i == 0: self.author = author
            else: self.replies[i-1]['author'] = author

        dates = response.css("td.postbottom")

        for i, date in enumerate(dates):

            date = ' '.join(date.css('::text').extract())

            if (len(dates)<len(replies)): j=i
            else:
                if (i % 2 == 0): j = i//2
                else: j = -1;

            if (j!=-1):
                if i == 0: self.date = date
                else: self.replies[j-1]['date'] = date

        avatars = response.css("div.postavatar::attr(src)")
        for i, avatar in enumerate(avatars):
            avatar = ' '.join(avatar.css('::text').extract())
            if i == 0: self.authorAvatar = avatar
            else: self.replies[i-1]['authorAvatar'] = avatar

        titles = response.css('div.postsubject')
        for i, title in enumerate(titles):
            title = ' '.join(title.css('::text').extract())

            if i == 0: self.title = title
            else: self.replies[i-1]['title'] = title

        self.parent = ''
        self.grandparent = ''

        if len(self.title) > 0:
            for i in reversed(range(1, 100)):
                self.parent = self.extractFirstElement(response.css('p.breadcrumbs > a:nth-child('+str(i)+')::text'))

                if self.parent != '':
                    self.parentIndex = i

                    self.grandparent = self.extractFirstElement(response.css('p.breadcrumbs > a:nth-child('+str(i-1)+')::text'))
                    if self.grandparent != '':
                        self.grandparentIndex = i-1
                        break

                    break


    def validate(self):
        if len(self.title) > 0:
            return 'topic'

        return ''