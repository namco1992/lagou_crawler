import scrapy
import logging
import re
from lagou.items import LagouItem


class LagouSpider(scrapy.Spider):
    name = "lagou"
    allowed_domains = ["lagou.com"]
    start_urls = [
        # "http://www.lagou.com/jobs/%d.html" % page for page in xrange(1952115, 1952120)
        "http://www.lagou.com/jobs/1952115.html"
    ]

    def parse(self, response):
        item = LagouItem()
        # item['keywords'] = response.css('')
        item['keywords'] = response.xpath('//meta[@name="keywords"]/@content').extract_first()
        item['job_desc'] = response.xpath('//dd[@class="job_bt"]/p/text()').extract()
        item['job_id'] = response.xpath('//*[@id="jobid"]/@value').extract_first()
        # item['tech_keywords'] = None
        logging.info(item)
        yield item
