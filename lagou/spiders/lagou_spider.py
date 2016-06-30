import os
import sys
import json

import scrapy
from lagou.items import LagouItem

PROJ_HOME = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJ_HOME)


class LagouSpider(scrapy.Spider):
    name = "lagou"
    allowed_domains = ["lagou.com"]

    def __init__(self, fullsize_crawl=False, *args, **kwargs):
        if fullsize_crawl is False:
            with open('../data/job_id_stats.json', 'r') as f:
                self.start_urls = [
                    "http://www.lagou.com/jobs/%d.html" % int(page) for page in json.load(f)
                ]
        else:
            self.start_urls = [
                "http://www.lagou.com/jobs/%d.html" % page for page in xrange(798605, 2000000)
            ]

    def parse(self, response):
        item = LagouItem()
        item['keywords'] = response.xpath('//meta[@name="keywords"]/@content').extract_first()
        item['job_desc'] = response.xpath('//dd[@class="job_bt"]/p/text()').extract()
        item['job_id'] = response.xpath('//*[@id="jobid"]/@value').extract_first()
        item['job_requests'] = response.xpath('//dd[@class="job_request"]/p/span/text()').extract()
        # logging.info(item)
        yield item
