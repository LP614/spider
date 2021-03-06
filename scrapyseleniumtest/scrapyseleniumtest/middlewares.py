# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import time

from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy import signals


class ScrapyseleniumtestSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ScrapyseleniumtestDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    def __init__(self, timeout):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('user-agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36"')
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        self.browser.set_window_size(1400, 700)
        self.browser.set_page_load_timeout(timeout)
        # 等待某个节点
        self.wait = WebDriverWait(self.browser, timeout)

    def __del__(self):
        self.browser.close()

    @classmethod
    def from_crawler(cls, crawler):
        s = cls(crawler.settings.get("SELENIUM_TIMEOUT"))
        # crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        self.browser.get(request.url)

        city_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#txtCity')))
        city_input.clear()
        city_input.send_keys('上海')

        check_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#txtCheckIn')))
        check_input.clear()
        check_input.send_keys('2018-12-07')

        checkout_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#txtCheckOut')))
        checkout_input.clear()
        checkout_input.send_keys('2018-12-10')

        room_inoput = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_roomCount')))
        room_inoput.click()

        room3_click = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//ul[@id="J_roomCountList"]/li[3]')))
        room3_click.click()

        person_click = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="J_RoomGuestInfoTxt"]')))
        person_click.click()

        ault_click = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//span[@id="J_AdultCount"]//i[@class="icon_numplus"]')))
        ault_click.click()
        ault_click.click()
        ault_click.click()

        childen_click = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//span[@id="J_ChildCount"]//i[@class="icon_numplus"]')))
        childen_click.click()

        # 选择小孩岁数
        # childen_input = self.wait.until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_childageVal0')))
        # childen_input.click()

        # childage_click = self.wait.until(
        #     EC.element_to_be_clickable((By.XPATH, '//ul[@id="J_childageVal0"]/option[3]')))
        # childage_click.click()

        # 小孩人数确定
        submit_input = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_RoomGuestInfoBtnOK')))
        submit_input.click()

        placesearch_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#txtKeyword')))
        placesearch_input.clear()
        placesearch_input.send_keys('')

        # 搜索
        button_search = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#btnSearch')))
        button_search.click()

        time.sleep(3)
        self.wait.until(EC.text_to_be_present_in_element_value((By.XPATH, '//input[@id="btnSearch"]'), str('搜索')))

        return HtmlResponse(url=request.url, body=self.browser.page_source, request=request, encoding='utf-8',
                            status=200)

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
