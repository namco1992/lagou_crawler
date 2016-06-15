import scrapy
import logging
from lagou.items import LagouItem


class LagouSpider(scrapy.Spider):
    name = "lagou"
    allowed_domains = ["lagou.com"]
    start_urls = [
        "http://www.lagou.com/jobs/%d.html" % page for page in xrange(500000, 2000000)
        # "http://www.lagou.com/jobs/1952115.html"
    ]

    def parse(self, response):
        item = LagouItem()
        item['keywords'] = response.xpath('//meta[@name="keywords"]/@content').extract_first()
        item['job_desc'] = response.xpath('//dd[@class="job_bt"]/p/text()').extract()
        item['job_id'] = response.xpath('//*[@id="jobid"]/@value').extract_first()
        item['job_requests'] = response.xpath('//dd[@class="job_request"]/p/span/text()').extract()
        # logging.info(item)
        yield item
