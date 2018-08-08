# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class VetItem(scrapy.Item):
    # define the fields for your item here like:
    report_name = scrapy.Field()
    report_url = scrapy.Field()
    report_text = scrapy.Field()
    report_niu_value = scrapy.Field()
