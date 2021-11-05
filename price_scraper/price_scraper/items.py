# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
# from price_tracker_backend.models import Product
from backend_api.models import Product

"""class PriceScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
"""


class PriceScraperItem(DjangoItem):
    django_model = Product
