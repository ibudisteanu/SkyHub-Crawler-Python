from Crawler.CrawlerBasic import CrawlerBasic
from Crawler.Crawlers.CrawlerPHPBB  import CrawlerPHPBB

class CrawlerTurkishajan(CrawlerPHPBB):

    name = 'CrawlerTurkishajan'

    url = 'http://turkishajan.com'
    domain = 'turkishajan.com'
    rejectionSubstr =  ["/memberlist.php?","/posting.php?","/search.php?","/ucp.php?","/cron.php?","/help-others/","/parteneri/"]

    start_urls = (url,)
    allowed_domains = [domain]

    removeLastMessage = True

    #CSS
    bodyFilterCSS = "#pagecontent"

    repliesCSS = "div.postbody"
    authorsCSS = "div.postauthor"
    datesCSS = "td.postbottom"
    avatarsCSS = "div.postavatar img"
    titlesCSS = "div.postsubject"

    breadcrumbsCSS = ''
    breadcrumbsChildrenCSS = 'p.breadcrumbs > a'