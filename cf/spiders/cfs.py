# -*- coding: utf-8 -*-
import scrapy


from cf.items import CfItem


class CfsSpider(scrapy.Spider):
    name = 'cfs'
    allowed_domains = ['codeforces.com']
    pages=41
    start_urls = []
    for i in range(pages):
        k=i+1
        start_urls.append('http://codeforces.com/problemset/page/{}'.format(k))


    def parse(self, response):
        sub=response.xpath('//div[@style="float: left;"]')
        items=[]
        for i in sub:
            item=CfItem()
            tmp=i.xpath('./a/@href').extract()[0]
            item['url']='http://codeforces.com'+tmp#相对改绝对
            a=tmp.split('/')
            item['title']=a[-2]+a[-1]+' '+i.xpath('./a/text()').extract()[0]#取题号
            item['title'].replace('\r\n','')
            yield scrapy.Request(item['url'],meta={'a':item},callback=self.ano_parse)#二级url爬取
    # def parse(self, response):
    #     url='http://codeforces.com/problemset/problem/935/D'
    #     item = CfItem()
    #     item['url']=url
    #     url=url.split('/')
    #     item['title'] = url[-2] + url[-1]
    #     item['title'].replace('\r\n','')
    #     yield scrapy.Request(item['url'],meta={'a':item},callback=self.ano_parse)

    def ano_parse(self,response):

        item=response.meta['a']#获取meta传值
        tl=response.xpath('//div[@class="time-limit"]/text()').extract()[0]
        ml=response.xpath('//div[@class="memory-limit"]/text()').extract()[0]
        stanum=response.xpath('//div[@class="problem-statement"]/div[2]//text()')
        sta=''
        for i in stanum:
            sta=sta+' '+i.extract()#保存statement部分
        item['lim']='time-limit : '+tl[0]+'memory-limit : '+ml[0]
        item['statement']=sta
        inspec=response.xpath('//div[@class="input-specification"]')
        outspec=response.xpath('//div[@class="output-specification"]')
        item['inspec'] =''
        item['outspec']=''
        item['sample']=''
        item['note']=''
        item['rbody']=response.body#保存response.body部分以便在pipeline.py里调用
        for i in inspec.xpath('.//p//text()'):
            item['inspec']=item['inspec']+' '+i.extract()
        for i in outspec.xpath('.//p//text()'):
            item['outspec']=item['outspec']+' '+i.extract()

        ex=response.xpath('//div[@class="sample-test"]')

        for i in ex.xpath('./div//text()'):
            item['sample']=item['sample']+' '+i.extract()+'\n'

        note=response.xpath('//div[@class="note"]//p//text()')#无视note标签下所有html标签读取字符

        for i in note:
            item['note']=item['note']+' '+i.extract()

        item['image_urls'] = []

        imgurl=response.xpath('//div[@class="problem-statement"]//img/@src')
        for j,i in enumerate(imgurl):
            item['image_urls'].append('http://codeforces.com'+i.extract().encode('utf8'))
            item['images']=j

        yield item
