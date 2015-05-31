from scrapy.spider import Spider
from bs4 import BeautifulSoup as bs
from cyzone.items import CyzoneItem
from scrapy.http import Request

class CyzoneSpider(Spider):
	name = "cyzone"
	allowed_domain = []
	start_urls = ["http://www.cyzone.cn/hotword/%E6%AF%8F%E6%97%A5%E8%9E%8D%E8%B5%84%E6%B8%85%E5%8D%95/"]


	def parse(self, response):
		soup = bs(response.body)
		items = soup.find_all("div", class_="item-info fl")
		for item in items:
			cyzone_item = CyzoneItem()
			cyzone_item["title"] = item.find("h2", class_="item-tit").get_text()
			cyzone_item["intro"] = item.find("p", class_="item-intro").get_text()
			url = item.find("a").get("href")
			cyzone_item["href"] = url
			yield scrapy.Request(url, callback=self.parseConent)
			# print(cyzone_item)
			yield cyzone_item

	def parseContent(self, response):
		soup = bs(response.body)
		title = soup.find('h1').get_text()
		content = soup.find('div', id='article-content')

