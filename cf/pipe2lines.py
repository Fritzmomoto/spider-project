#coding:utf8

from scrapy.pipelines.images import ImagesPipeline
import shutil
from cf.settings import IMAGES_STORE
import scrapy
from scrapy.http import Request

print("===================")


class Picpipline(ImagesPipeline):

    print("11111111111111111111111111")
    def get_media_requests(self, item, info):
        for i in item['image_urls']:
            yield Request(i)

    def item_completed(self, results, item, info):
        ipath=[x['path'] for ok,x in results if ok]
        shutil.move(IMAGES_STORE+'/'+ipath[0],item['paths'])
        yield item
