import scrapy


class JumiaSpiderSpider(scrapy.Spider):
    name = 'jumia_spider'
    allowed_domains = ['jumia.co.ke']
    start_urls = ['http://jumia.co.ke/']

    def start_requests(self):
        urls = [
            'https://www.jumia.co.ke/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        pass
