# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    detailLink = scrapy.Field()
    title = scrapy.Field()
    communityName = scrapy.Field()
    areaName = scrapy.Field()
    totalPrice = scrapy.Field()
    unitPrice = scrapy.Field()

    # area = scrapy.Field()
    # priceInfo = scrapy.Field()
    # focus_num = scrapy.Field()
    # watch_num = scrapy.Field()
    # time = scrapy.Field()
    # price = scrapy.Field()
    # averagePrice = scrapy.Field()
    # link = scrapy.Field()
    # Latitude = scrapy.Field()
    # city = scrapy.Field()
