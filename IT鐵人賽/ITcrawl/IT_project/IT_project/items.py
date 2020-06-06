# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ProductItem(scrapy.Item):
    Brand = scrapy.Field()
    StyleNumber = scrapy.Field()
    Name = scrapy.Field()
    Bullets = scrapy.Field()
    Description = scrapy.Field()
    Gender = scrapy.Field()
    Sport = scrapy.Field()
    Clothing = scrapy.Field()
    Size = scrapy.Field()
    MinPrice = scrapy.Field()
    MaxPrice = scrapy.Field()
    Color = scrapy.Field()
    Url = scrapy.Field()
    ImageUrl = scrapy.Field()
    ReviewNumber = scrapy.Field()
    AverageRating = scrapy.Field()