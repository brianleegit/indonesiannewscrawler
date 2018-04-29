import scrapy   
import pymongo
import datetime
from scrapy.utils.project import get_project_settings
from kompas.items import ArticleLinkItem


class LinkSpider(scrapy.Spider):    
    name            = "link"
    allowed_domains = ['kompas.com']    
    # project settings
    settings  = get_project_settings()
    category  = None
    def start_requests(self):  
        # get kompas categories and links
        client       = pymongo.MongoClient(self.settings.get('MONGO_URI'))
        db           = client[self.settings.get('MONGO_DATABASE')]
        # for specific query
        query = {"status" : 0}       
        if (self.category != None):
            query["name"] = self.category        
        # generate url from date range        
        for link in db.categories.find(query, {"link":1,"_id":0}):
            # date ranges                        
            start = datetime.date(2014, 1, 1)             # start date
            delta = datetime.date.today() - start         # timedelta
            date_list = []
            for i in range(delta.days + 1):
                date_list.append(start + datetime.timedelta(days=i))
            for date in date_list:
                yield scrapy.Request('{0}／search/{1}'.format(link["link"], date))       
                
    
    def parse(self, response):
        cat = response.url.split("/")[2].split('.')[0]
        item = ArticleLinkItem()
        for article in response.css("div.article__list"):
            article_url                     = article.css('div.article__list__title a.article__link::attr(href)').extract_first()
            if(article_url != ""):
                item["article_title"]           = article.css('div.article__list__title a.article__link::text').extract_first()
                item["article_url"]             = article_url
                item["article_category"]        = cat
                item["article_sub_category"]    = article.css('div.article__list__info div.article__subtitle::text').extract_first()
                article_datetime                = article.css('div.article__list__info div.article__date::text').extract_first().split(',')
                item["article_post_date"]       = article_datetime[0]
                item["article_post_time"]       = article_datetime[1].split()[0]
                item["status"]                  = 0
                yield item
            

        next_page = response.css("a[rel='next'].paging__link--next::attr(href)").extract_first()
        if next_page is not None:
            self.log("Next page is followed : %s" % next_page)
            yield scrapy.Request(next_page, callback=self.parse)
