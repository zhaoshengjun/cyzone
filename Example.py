#request with cookies
request_with_cookies = Request(url="http://www.example.com",cookies=[{
	'name':'currency',
	'value':'USD',
	'domain':'example.com',
	'path':'/currency'}])

#passsing additional data to callback functions
def parse_page(self, response):
	item = MyItem()
	item['main_url'] = response.url
	request = scrapy.Request("http://www.example.com", callback=self.parse_page2)
	request.meta['item'] = item
	return request
def parse_page2(self, response):
	item = response.meta['item']
	item['other_url'] = response.url
	return item

#using FromRequest to send data via HTTP Post
return [FromRequest(url='http://www.example.com',
	formdata={'name':'John Doe','age':'27'},
	callback=self.after_post)]

#simluate user login
import scrapy
class LoginSpider(scrapy.Spider):
	name = 'exmaple.com'
	start_urls = ['http://www.example.com/login.php']

	def parse(self, response):
		return scrapy.FromRequest.form_response(
			response,
			formdata={'username':'john', 'passsword':'secret'},
			callback=self.after_login)
	def after_login(self, response):
		if 'authentication falied' in response.body:
			self.log('login falied', level=log.ERROR)
		item = MyItem()
		return item
