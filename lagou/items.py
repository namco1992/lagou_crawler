# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouItem(scrapy.Item):
    # define the fields for your item here like:
    keywords = scrapy.Field()
    job_desc = scrapy.Field()
    job_id = scrapy.Field()
    tech_keywords = scrapy.Field()
    job_requests = scrapy.Field()
