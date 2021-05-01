# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BilibiliItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class BiliBiliData(scrapy.Item):
    aid = scrapy.Field()
    pubdate = scrapy.Field()
    view = scrapy.Field()
    like = scrapy.Field()
    danmaku = scrapy.Field()
    reply = scrapy.Field()
    favorite = scrapy.Field()
    coin = scrapy.Field()
    share = scrapy.Field()

