# Scrapy settings for sjbizhi project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'sjbizhi'

SPIDER_MODULES = ['sjbizhi.spiders']
NEWSPIDER_MODULE = 'sjbizhi.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'sjbizhi (+http://www.yourdomain.com)'


ITEM_PIPELINES = {
    'sjbizhi.pipelines.DownloadPicPipeline': 888,
}

IMAGES_EXPIRES = 90
IMAGES_STORE = '/data/program/sjbizhi/picdown/'
