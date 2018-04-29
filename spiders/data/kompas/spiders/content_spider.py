import scrapy   
import pymongo
import datetime
from scrapy.utils.project import get_project_settings
from kompas.items import ArticleLinkItem


class ContentSpider(scrapy.Spider):    
    name            = "content"
    allowed_domains = ['kompas.com']    
    # project settings
    settings  = get_project_settings()
    category  = None
    def start_requests(self):  
        return(True)