import scrapy
from kompas.items import CategoryItem

class CategoriesSpider(scrapy.Spider):
    name = "categories"
    start_urls = [
        'https://www.kompas.com/'
    ]

    def parse(self, response):
        item = CategoryItem()
        for cat in response.css('ul.nav__row > li'):           
            category = cat.css('a.nav__link::text').extract_first().lower()
            if(category not in 'vik kolom images tv'):
                item["name"] = category
                item["link"] = cat.css('a.nav__link::attr(href)').extract_first() 
                item["status"] = 0            
                yield item





