import requests
import json
from lxml import etree
from dailichi import get_proxy
from agent_helper import get_random_agent
import time
import random
import pymongo


class Qichamao:

	def __init__(self):
		agent = get_random_agent()
		
		self.url = 'https://www.qichamao.com/cert-wall'

		self.headers = {
			'Referer': 'https://www.qichamao.com/cert-wall/',
			'User-Agent': agent,
			'Host': 'www.qichamao.com',
			'Accept': 'application/json, text/plain, */*',
			'Accept-Encoding': 'gzip, deflate, sdch',
			'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2,mt;q=0.2',
			'Connection': 'keep-alive',
			'X-Requested-With': 'XMLHttpRequest',
		}
		
		print(self.headers)

		self.session = requests.Session()

	def parse_page(self, html):
		selector = etree.HTML(html)
		company_items = selector.xpath('//div[@class="firmwall_list_box"]')
		company_list = []
		for company_item in company_items:
			company_dict = {}
			company_name = company_item.xpath('.//*[@class="firmwall_list_tit toe"]/a/text()')[0]
			company_dict['company_name'] = company_name

			company_list.append(company_dict)

		return company_list

	def get_page(self):
		proxy = get_proxy()
		proxies = {
			'http': 'http://' + proxy,
			'https': 'https://' + proxy,
		}
		response = requests.get(self.url, headers=self.headers, proxies=proxies)
		if response.status_code == 200:
			return response.content.decode('utf-8')
		else:
			return None

	def post_page(self, page, pagesize, proxies=None):
		data = {'page': page, 'pagesize': pagesize}
		
		# 设置代理
		print(proxies)
		sleep_time = random.randint(1, 3)
		time.sleep(sleep_time)
		response = None
		if proxies is None:
			response = requests.post(self.url, headers=self.headers, data=data)
		else:
			response = requests.post(self.url, proxies=proxies, headers=self.headers, data=data)

		if response.status_code == 200:
			return response.content.decode('utf-8')
		else:
			return None

	def parse_json(self, json_text):
		print('**********')
		print(json_text)
		result_json = json.loads(json_text)
		if not result_json['isSuccess']:
			return None

		data_list = result_json['dataList']
		for data in data_list:
			insert_company(data)
			print(data['CompanyName'])

		return data_list


def insert_company(companies):
	client = pymongo.MongoClient(host='localhost', port=27017)
	db = client.company
	collection = db.comoany_list
	collection.insert(companies)


def main():
	qichamao = Qichamao()
	html = qichamao.get_page()
	results = qichamao.parse_page(html)
	print('page 1')
	print('*' * 20)
	for item in results:
		print(item['company_name'])

	# for i in range(100):
		# print('page %d' % (i + 2))
		# print('*' * 20)
		#
		# json_text = None
		# try:
		# 	json_text = qichamao.post_page(i + 2, 9)
		# except Exception as e:
		# 	while (True):
		# 		proxies = get_proxies()
		# 		json_text = qichamao.post_page(i + 2, 9, proxies)
		# 		if json_text is not None:
		# 			print('except break')
		# 			break
		#
		# if json_text is None:
		# 	while(True):
		# 		proxies = get_proxies()
		# 		json_text = qichamao.post_page(i + 2, 9, proxies)
		# 		if json_text is not None:
		# 			print('none break')
		# 			break
		#
		# if json_text is not None:
		# 	result = qichamao.parse_json(json_text)
		# 	if result is None:
		# 		proxies = get_proxies()
		# 		json_text = qichamao.post_page(i + 2, 9, proxies)
		# 		if json_text is not None:
		# 			result = qichamao.parse_json(json_text)


if __name__ == '__main__':
	main()
