# -*- coding: utf-8 -*-
import scrapy


class JianshuSpider(scrapy.Spider):
    name = 'jianshu'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/']

    def parse(self, response):
        pass
