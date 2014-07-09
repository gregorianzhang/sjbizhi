from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from sjbizhi.items import SjbizhiItem
from scrapy.http import Request


class DownpicSpider(CrawlSpider):
    name = 'downpic'
    allowed_domains = ['pic.hiapk.com']
    start_urls = ['http://pic.hiapk.com/sjbizhi/list_325_1.html']

    rules = (
        Rule(SgmlLinkExtractor(allow=r'/list_325_\d+\.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        sel = Selector(response)
        #print response.url
        #i['domain_id'] = sel.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = sel.xpath('//div[@id="name"]').extract()
        #i['description'] = sel.xpath('//div[@id="description"]').extract()
        picurl = sel.xpath('//*[@class="tit"]/a/@href').extract()
        for url in picurl:
            #print url
            yield Request(url, callback=self.pic_page)

    def pic_page(self, response):
        sel = Selector(response)
        pic = sel.xpath('//*[@class="clearfix"]/li/a/img/@data-bigimg').extract()
        items = []
        i = SjbizhiItem()
        i['url'] = pic
        items.append(i)
        print items
        return items
#        print "url type is %s  and url is %s" % (type(pic),pic)
#        return pic
