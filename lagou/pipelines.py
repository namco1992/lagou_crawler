# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
import traceback
import logging

from pymongo import MongoClient
from scrapy.exceptions import DropItem

from lagou.settings import FILTER_LIST


class CleanDataPipeline(object):
    def process_item(self, item, spider):
        required_list = set()
        for desc in item['job_desc']:
            keywords = re.findall(ur'[a-zA-Z/\s]{2,}', desc)
            if len(keywords) > 0:
                required_list.update((x.strip().lower() for x in keywords))
        required_list = list(required_list)
        item['tech_keywords'] = required_list
        del item['job_desc']
        # logging.info('=======required_list: %s', item['tech_keywords'])
        return item


class FilterPipeline(object):

    def process_item(self, item, spider):
        # 检查是否获取到所需信息
        if not item['job_id']:
            raise DropItem("Missing needed info: %s" % item)
        # 暂时不判断职位是否过期
        # 判断是否属于指定职位的信息
        if any((x.decode('utf-8') in item['keywords'] for x in FILTER_LIST)):
            del item['keywords']
            logging.info('Captured one.')
            return item
        else:
            # return
            raise DropItem("Job not match.")


class MongoPipeline(object):

    # collection_name = 'scrapy_items'

    def __init__(self, mongo_uri, mongo_db, collection_name):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.collection_name = collection_name

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'test'),
            collection_name=crawler.settings.get('COLLECTION_NAME', 'test')
        )

    def open_spider(self, spider):
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        # 将 job_id 设为唯一键
        # 如果由于 job_id 重复则记录 log
        collection = self.db[self.collection_name]
        try:
            collection.replace_one({'job_id': item['job_id']}, dict(item), True)
        except Exception, e:
            logging.warn(traceback.format_exc())
        finally:
            return item
