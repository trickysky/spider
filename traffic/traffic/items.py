# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SiweiItem(scrapy.Item):
    city = scrapy.Field()
    code = scrapy.Field()
    time = scrapy.Field()
    speed = scrapy.Field()
    road_name = scrapy.Field()
    start_name = scrapy.Field()
    end_name = scrapy.Field()
    dir = scrapy.Field()
    b_index = scrapy.Field()
    c_index = scrapy.Field()
    s_index = scrapy.Field()
    kind = scrapy.Field()
    rtic_lon_lats = scrapy.Field()
    vkt = scrapy.Field()