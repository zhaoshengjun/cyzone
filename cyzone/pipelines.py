# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class CyzonePipeline(object):
#     def process_item(self, item, spider):
#         return item
# from pymongo import MongoClient
import pymongo
from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log

class MongoDBPipeline(object):

	def __init__(self):
		connection = pymongo.MongoClient(
			settings['MONGODB_SERVER'],
			settings['MONGODB_PORT']
			)
		db = connection[settings['MONGODB_DB']]
		self.collection = db[settings['MONGODB_COLLECTION']]
		# client  = MongoClient()
		# # print(client)
		# db = client['test']
		# self.collection = db['VCNEWS']

	def process_item(self, item, spider):
		valid = True
		for data in item:
			# invalid scenario 1 - no data
			if not data:
				valid = False
				raise DropItem("Missing {0}!".format(data))
			# invalid scenario 2 - existing record
			href = item["href"]
			exist_record = self.collection.find({"href":href}).count()
			if exist_record > 0:
				print(self.collection.find({"href":href}))
				raise DropItem('Record has already been added')
		if valid:
			# print(item)
			self.collection.insert(dict(item))
			# self.collection.update({"href": item['href']}, dict(item), upsert=true)
			log.msg('Added to MongoDB database.', level=log.DEBUG, spider=spider)
		return item
