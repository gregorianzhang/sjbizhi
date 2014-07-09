# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.contrib.pipeline.images import ImagesPipeline
import re
from scrapy.http import Request


class SjbizhiPipeline(object):
    def process_item(self, item, spider):
        return item

class DownloadPicPipeline(ImagesPipeline):

     def get_media_requests(self, item, info):
        for url in item['url']:
            yield Request(url)
