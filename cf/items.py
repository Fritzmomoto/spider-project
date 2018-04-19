# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CfItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url=scrapy.Field() #题目详情页面url
    title=scrapy.Field() #题号
    lim=scrapy.Field()#时间空间限制
    statement=scrapy.Field()#描述部分
    inspec=scrapy.Field()#输入样例部分
    outspec=scrapy.Field()#输出样例部分
    sample=scrapy.Field()#样例
    note=scrapy.Field()#题目note部分
    rbody=scrapy.Field()#response.body
    image_urls=scrapy.Field()#图片链接（list）
    paths=scrapy.Field()#题目保存路径
    images=scrapy.Field()