from bs4 import BeautifulSoup as bs
from cyzone.items import CyzoneItem
from scrapy.http import Request
from scrapy.spider import Spider
# from scrapy.contrib.spiders import CrawlSpider, Rule
# from scrapy.contrib.linkextractors import LinkExtractor

class CyzoneSpider(Spider):
	name = "cyzone"
	allowed_domain = []
	# start_urls = ["http://www.cyzone.cn/hotword/%E6%AF%8F%E6%97%A5%E8%9E%8D%E8%B5%84%E6%B8%85%E5%8D%95/"]

	def __init__(self, name=None, **kwargs):
		urls = []
		base_url = "http://www.cyzone.cn/hotword/%E6%AF%8F%E6%97%A5%E8%9E%8D%E8%B5%84%E6%B8%85%E5%8D%95/"
		for i in range(1,4):
			url = base_url + str(i)
			urls.append(url)
		# print(urls)
		self.start_urls = urls


	def parse(self, response):
		soup = bs(response.body)
		# generate requests from the page list
		requests = []
		items = soup.find_all("div", class_="item-info fl")
		for item in items:
			cyzone_item = CyzoneItem()
			cyzone_item["title"] = item.find("h2", class_="item-tit").get_text()
			cyzone_item["intro"] = item.find("p", class_="item-intro").get_text()
			url = item.find("a").get("href")
			cyzone_item["href"] = url
			request = Request(url, callback=self.parse_page)
			request.meta['item'] = cyzone_item
			requests.append(request)
		return requests

	def parse_page(self, response):
		item = response.meta['item']
		soup = bs(response.body)
		item['contents'] = soup.find("div", id="article-content").get_text()
		return item

# class CyzoneSpider(CrawlSpider):
#   name = "cyzone"
#   start_urls = ['http://www.cyzone.cn/hotword/%E6%AF%8F%E6%97%A5%E8%9E%8D%E8%B5%84%E6%B8%85%E5%8D%95']
#   rules = (Rule(LinkExtractor(allow=[r'/\d+']), follow=True),Rule(LinkExtractor(allow=[r'/a\d{8}/\d{6}']), callback='parse_page'))
#   def parse_page(self, response):
#     soup = bs(response.body)
#     cyzone_item = CyzoneItem()
#     cyzone_item["title"] = soup.title
#     cyzone_item["intro"] = soup.find("p",class_="article-introduction").get_text()
#     cyzone_item["href"] = response.url
#     cyzone_item["contents"] = soup.find("div", id="article-content").get_text()
#     return cyzone_item


# class CyzoneSpider(Spider):
	# name = "cyzone"
	# allowed_domain = []
	# start_urls = ["http://www.cyzone.cn/hotword/%E6%AF%8F%E6%97%A5%E8%9E%8D%E8%B5%84%E6%B8%85%E5%8D%95/"]

	# def parse(self, response):
	# 	soup = bs(response.body)
	# 	# generate requests from the page list
	# 	self.parse_list(response)
	# 	# generate requests from the following pages
	# 	follow_pages = soup.find_all("div", id="pages")
	# 	for page in follow_pages:
	# 		url = page.find("a").get("href")
	# 		# In case the URL doesn't start with "http"
	# 		if url[0:3] != "http":
	# 			url = "http://www.cyzone.cn"+url
	# 		yield self.make_request_from_url(url)

	# def make_request_from_url(self, url):
	# 	return Request(url, callback=self.parse_list,dont_filter=True)

	# def parse_list(self, response):
	# 	soup = bs(response.body)
	# 	items = soup.find_all("div", class_="item-info fl")
	# 	for item in items:
	# 		yield self.make_request_from_list(item)

	# def make_request_from_list(self, item):
	# 	cyzone_item = CyzoneItem()
	# 	cyzone_item = CyzoneItem()
	# 	cyzone_item["title"] = item.find("h2", class_="item-tit").get_text()
	# 	cyzone_item["intro"] = item.find("p", class_="item-intro").get_text()
	# 	url = item.find("a").get("href")
	# 	cyzone_item["href"] = url
	# 	request = Request(url, callback=self.parse_page,dont_filter=True)
	# 	request.meta['item'] = cyzone_item
	# 	return request

	# def parse_page(self, response):
	# 	item = response.meta['item']
	# 	soup = bs(response.body)
	# 	item['contents'] = soup.find("div", id="article-content").get_text()
	# 	return item