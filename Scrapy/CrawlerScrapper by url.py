# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 09:57:32 2022

@author: Ivan Tonatiuh
"""


from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class CrawlingSpider(CrawlSpider):
    name:"mycrawler"
    allowed_domains=["toscrape.com"]
    start_url=["http://books.toscrape.com/"]
    
    rules = (
        Rule(LinkExtractor(allow="catalogue/category")),
        )
    
    