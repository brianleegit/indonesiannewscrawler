# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CategoryItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    link = scrapy.Field()
    status = scrapy.Field()
    pass

class ArticleLinkItem(scrapy.Item):
    # define the fields for your item here like:
    article_url = scrapy.Field()
    article_title = scrapy.Field()
    article_category = scrapy.Field()
    article_sub_category = scrapy.Field()
    article_post_date = scrapy.Field()
    article_post_time = scrapy.Field()
    status = scrapy.Field()
    pass