# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class PriceScraperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter.get('current_price'):
            adapter.update({'current_price': adapter.get('current_price').replace('$', '')})
            item.save()
            return item
        else:
            raise DropItem("Missing current_price in %s" % item)
