# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class PriceScraperPipeline:
    def __init__(self):
        self.names_seen = set()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if not adapter.get('current_price'):
            raise DropItem("Missing current_price in %s" % item)
        # adapter.update({'current_price': adapter.get('current_price').replace('$', '')})
        if adapter.get('name') in self.names_seen:
            raise DropItem("Duplicate item found: %s" % item)
        self.names_seen.add(adapter.get('name'))
        item.save()
        return item
