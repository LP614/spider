# -*- coding: utf-8 -*-
import scrapy

from maoyan.items import MaoyanItem


class CatSpider(scrapy.Spider):
    name = 'cat'
    allowed_domains = ['sports.sina.com.cn']
    start_urls = ['http://sports.sina.com.cn/g/2018worldcupeq/']

    def parse(self, response):
        movie_names = response.css('.headline a::text').extract()
        for movie_name in movie_names:
            maoyam_item = MaoyanItem()
            maoyam_item['name'] = movie_name
            yield maoyam_item


