# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose,TakeFirst

class JianshuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

def getText(value):
    try:
        follows = value[1]
    except:
        follows = ''
    return follows

class UserItem(scrapy.Item):
    # name = scrapy.Field()
    follows = scrapy.Field(
        # input_processor=MapCompose(getText),
        # output_processor=TakeFirst()
    )
    fans = scrapy.Field(
        # input_processor=MapCompose(getText),
        # output_processor=TakeFirst()
    )
    articles = scrapy.Field(
        # input_processor=MapCompose(getText),
        # output_processor=TakeFirst()
    )
    words = scrapy.Field(
        # input_processor=MapCompose(getText),
        # output_processor=TakeFirst()
    )
    likes = scrapy.Field(
        # input_processor=MapCompose(getText),
        # output_processor=TakeFirst()
    )
    moneys = scrapy.Field(
        # input_processor=MapCompose(getText),
        # output_processor=TakeFirst()
    )
