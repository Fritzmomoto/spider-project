# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import scrapy
import time
import pdfkit
import urllib2

html_template = u"""
<!DOCTYPE html>

<html>
    <head>
        <meta charset="utf-8" />
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    </head>
    <body>
        <!-- <center><h1>{title}</h1></center> -->
        {content}
    </body>
</html>
"""


class CfPipeline(object):
    def process_item(self, item, spider):
        a=item['url'].split('/')
        dirname=a[-2]+a[-1]
        path='/home/momoto/code/cfspider/'+dirname
        item['paths']=path
        os.makedirs(path)
        path=path+'/'
        temppath=path
        file=['Statement.txt','Input-specification.txt','Output-specification.txt','Limit.txt','Sample-test.txt','Note.txt']
        itemname=['statement','inspec','outspec','lim','sample','note']
        for j,i in enumerate(file):#把数据写入对应文件
            temppath=path+file[j]
            with open(temppath,'a') as fp:
                fp.write(item[itemname[j]].encode('utf8')+'\n')
        if item['image_urls']:#如果有图片的话，则使用urllib2库下载
            for j,i in enumerate(item['image_urls']):
                request = urllib2.Request(i)
                response = urllib2.urlopen(request).read()
                with open(path+str(j)+'.png','wb') as f:  #保存图片
                    f.write(response)

        with open (path+dirname+'.html','a') as fp:
            fp.write(item['rbody'].replace('src="/predownloaded/', 'src="http://codeforces.com/predownloaded/'))#将图片的相对路径改成绝对路径并保存为html
        options = {
            'page-size': 'Letter',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': "UTF-8",
        }
        pdfkit.from_url(path+dirname+'.html',path+dirname+'.pdf',options=options)#html转pdf
        return item



    # url='http://codeforces.com/predownloaded/c6/6b/c66bf8ecc5d9ef3b7001a32bf05d4a0d784f311b.png'
    #
    # request = urllib2.Request(url)
    # response = urllib2.urlopen(request).read()
    #
    # with open('image.png','wb') as f:  #保存图片
    #     f.write(response)
