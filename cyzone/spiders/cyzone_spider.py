from bs4 import BeautifulSoup as bs
from cyzone.items import CyzoneItem
from scrapy.http import Request
from scrapy.spider import Spider

class CyzoneSpider(Spider):
	name = "cyzone"
	allowed_domain = []
	start_urls = ["http://www.cyzone.cn/hotword/%E6%AF%8F%E6%97%A5%E8%9E%8D%E8%B5%84%E6%B8%85%E5%8D%95/"]

	def parse(self, response):
		soup = bs(response.body)
		self.parse_list(response)
		# Follow pages
		requests = []
		follow_pages = soup.find_all("div", id="pages")
		for page in follow_pages:
			url = page.find("a").get("href")
			# In case the URL doesn't start with "http"
			if url[0:3] != "http":
				url = "http://www.cyzone.cn"+url
			request = Request(url, callback=self.parse_list)
			requests.append(request)
		return requests

	def parse_list(self, response):
		soup = bs(response.body)
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