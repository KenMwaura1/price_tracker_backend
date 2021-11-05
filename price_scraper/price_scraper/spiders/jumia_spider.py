import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from ..items import PriceScraperItem


class JumiaSpiderSpider(CrawlSpider):
    name = 'jumia_spider'
    allowed_domains = ['jumia.co.ke']
    start_urls = ['https://www.jumia.co.ke/mlp-black-friday/',
                  # 'https://www.jumia.co.ke/groceries/'
                  ]
    total_pages = 40
    rules = [Rule(LinkExtractor(allow=r'page=\d+'), callback='parse_item', follow=True)]

    def parse_item(self, response):
        if response.status == 200 and response.css('.core'):
            scraped_product = PriceScraperItem()
            scraped_product['name'] = response.css('.name::text').get()
            scraped_product['current_price'] = response.css('div.prc::text').get()
            scraped_product['old_price'] = response.css('div::attr(data-oprc)').get()
            scraped_product['image_url'] = response.css('img.img::attr(data-src)').get()
            scraped_product['discount'] = response.css('div._dsct::text').get()
            scraped_product['link'] = self.start_urls[0] + response.css('a.core::attr(href)').get()
            scraped_product['category'] = response.css('a.core::attr(data-category)').get()
            yield scraped_product
        else:
            print('No products found')



    def parse(self, response):
        next_page = response.css('a.pg').xpath('@href')[2].get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

