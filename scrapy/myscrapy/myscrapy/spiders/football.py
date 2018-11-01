# -*- coding: utf-8 -*-
import scrapy
from myscrapy.items import FootballItem


class FootballSpider(scrapy.Spider):
    name = 'football'
    allowed_domains = ['sports.sina.com.cn']
    start_urls = ['http://sports.sina.com.cn/g/2018worldcupeq/']

    def parse(self, response):
        headlines = response.selector.css('.headline')
        for headline in headlines:
            # print(headline)
            headline_txt = headline.css('a::text').extract_first()
            item = FootballItem()
            item['text'] = headline_txt
            yield item
