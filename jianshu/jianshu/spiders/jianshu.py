# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from jianshu.items import UserItem

class JianshuSpider(scrapy.Spider):
    '''
    爬取某用户的详细信息
    爬取用户的 关注数 、 粉丝数 、 文章数 、 字数 、 收获喜欢 、 总资产
    爬取用户文章详情
    通过用户信息里的文章数，分析该用户需要处理的链接数
    每一个  https://www.jianshu.com/u/a4a7b9d0c23e?order_by=shared_at&page=1 链接里面含有九篇文章
    通过文章数 计算出需要处理的链接数
    '''
    name = 'jianshu'
    allowed_domains = ['jianshu.com']
    # start_urls 修改后面的id成想获取的用户的id
    start_urls = ['https://www.jianshu.com/u/a4a7b9d0c23e']

    def parse(self, response):
        userItemLoader = ItemLoader(item = UserItem(), response=response)
        # userItemLoader.add_xpath('name', '')

        '''
        ItemLoader.xpath() 返回最后是一个空值
        但是通过scrapy shell 测试了 xpath是可以获取值的
        现将itemLoader方法换成Item填充
        '''
        # userItemLoader.add_xpath('follows', '//div[@class="info"]/ul/li[1]/div/a/p/text()')
        # userItemLoader.add_xpath('fans', '//div[@class="info"]/ul/li[2]/div/a/p/text()')
        # userItemLoader.add_xpath('articles', '//div[@class="info"]/ul/li[3]/div/a/p/text()')
        # userItemLoader.add_xpath('words', '//div[@class="info"]/ul/li[4]/div/p/text()')
        # userItemLoader.add_xpath('likes', '//div[@class="info"]/ul/li[5]/div/p/text()')
        # userItemLoader.add_xpath('moneys', '//div[@class="info"]/ul/li[6]/div/p/text()')
        # userInfo = userItemLoader.load_item()
        # yield userInfo

        # ItemLoader 填充方式
        # 该方式可以获取对应的值
        userInfo = UserItem()
        userInfo['follows'] = response.xpath('//div[@class="info"]/ul/li[1]/div/a/p/text()').getall()
        userInfo['fans'] = response.xpath('//div[@class="info"]/ul/li[2]/div/a/p/text()').getall()
        userInfo['articles'] = response.xpath('//div[@class="info"]/ul/li[3]/div/a/p/text()').getall()
        userInfo['words'] = response.xpath('//div[@class="info"]/ul/li[4]/div/p/text()').getall()
        userInfo['likes'] = response.xpath('//div[@class="info"]/ul/li[5]/div/p/text()').getall()
        userInfo['moneys'] = response.xpath('//div[@class="info"]/ul/li[6]/div/p/text()').getall()
        yield userInfo
