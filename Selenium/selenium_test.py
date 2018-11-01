import time
import random
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import quote
from lxml import etree

# 无头浏览器
from my_mysql import MyMysql

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)

# browser = webdriver.Chrome()
browser.set_window_size(1400, 700)
wait = WebDriverWait(browser, 10)
KEYWORD = '笔记本电脑'


# def get_page():
# 	url = 'https://s.taobao.com'
# 	browser.get(url)
# 	input = wait.until(
# 		EC.presence_of_element_located((By.CSS_SELECTOR, '.search-combobox-input')))
# 	input.clear()
# 	input.send_keys(KEYWORD)
#
# 	submit = wait.until(
# 		EC.element_to_be_clickable((By.CSS_SELECTOR, '.search-button .btn-search')))
# 	submit.click()
#
# 	login_link = wait.until(
# 		EC.element_to_be_clickable((By.CSS_SELECTOR, '.login_links .forget-pwd.J_Quick2Static')))
# 	login_link.click()
#
# 	username_input = wait.until(
# 		EC.presence_of_element_located((By.CSS_SELECTOR, '#TPL_username_1')))
# 	username_input.clear()
# 	username_input.send_keys('')


def index_page(page):
	if page == 1:
		url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
		# print(url)
		browser.get(url)

	for i in range(8):
		str_js = 'var step = document.body.scrollHeight / 8; window.scrollTo(0, step * %d)' % (i+1)
		browser.execute_script(str_js)
		time.sleep(1)

	browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
	if page > 1:
		input = wait.until(
			EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))

		submit = wait.until(
			EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit')))
		input.clear()
		input.send_keys(page)

		submit.click()
		wait.until(
			EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page)))
		wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
	
	page_source = browser.page_source

	return page_source


def parse_page(page_source):
	etree_html = etree.HTML(page_source)
	print(type(etree_html))
	products = etree_html.xpath('//div[@id="mainsrp-itemlist"]//div[@class="items"][1]//div[contains(@class, "item")]')

	print(len(products))

	for product in products:
		items = {}
		items['price'] = product.xpath('.//div[contains(@class, "price")]/strong/text()')[0].strip()
		items['title'] = product.xpath('.//div[contains(@class, "title")]/a/descendant::*')
		items['shop'] = product.xpath('.//div[contains(@class, "shop")]/a/span[2]/text()')[0].strip()
		items['image'] = product.xpath('.//div[@class="pic"]//img[contains(@class, "img")]/@data-src')[0].strip()
		items['deal'] = product.xpath('.//div[contains(@class, "deal-cnt")]//text()')[0]
		items['location'] = product.xpath('.//div[contains(@class, "location")]//text()')[0]
		yield items


def main():
	info = MyMysql('localhost', 3306, 'root', '123456', 'spider', 'utf8')
	for page in range(100):
		page_source = index_page(page + 1)

		# products = parse_page(page_source)
		# for product in products:
		# 	print(product['title'])
		# 	print(product['price'])
		items = parse_page(page_source)
		# print(items)
		for item in items:
			sql = 'insert into selenium_taobao_two(price, title, shop, image, deal, localtion) values("%s", "%s", "%s", "%s", "%s", "%s")' % (item['price'], item['title'], item['shop'], item['image'], item['deal'], item.get('localtion') if item.get('localtion') else '')
			info.insert_info(sql)
			print(item)


if __name__ == '__main__':
	main()