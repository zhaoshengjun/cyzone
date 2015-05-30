# -*- coding: utf-8 -*-

# Scrapy settings for cyzone project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'cyzone'

SPIDER_MODULES = ['cyzone.spiders']
NEWSPIDER_MODULE = 'cyzone.spiders'
ITEM_PIPELINES = {'cyzone.pipelines.MongoDBPipeline':1}
# MONGODB_SERVER = 'localhost'
# MONGODB_PORT = 27017
# MONGODB_DB = 'TEST'
# MONGODB_COLLECTION = 'VCMOVE'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'cyzone (+http://www.yourdomain.com)'
