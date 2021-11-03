import scrapy


class JumiaSpiderSpider(scrapy.Spider):
    name = 'jumia_spider'
    allowed_domains = ['jumia.co.ke']
    start_urls = ['http://jumia.co.ke/']

    def parse(self, response):
        pass
