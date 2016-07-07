# -*-coding:utf-8-*-
import logging
import random

from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
from scrapy import signals

from lagou.settings import UALIST


class RotateUserAgentMiddleware(UserAgentMiddleware):

    def __init__(self, user_agent=''):
        self.user_agent = user_agent

    @classmethod
    def from_crawler(cls, crawler):
        o = cls(crawler.settings['USER_AGENT'])
        crawler.signals.connect(o.spider_opened, signal=signals.spider_opened)
        return o

    def spider_opened(self, spider):
        self.user_agent = getattr(spider, 'user_agent', self.user_agent)

    def process_request(self, request, spider):
        # if self.user_agent:
        user_agent = random.choice(UALIST)
        # 显示当前使用的useragent
        # print "********Current UserAgent:%s************" % user_agent
        # 记录
        # logging.debug('Current UserAgent: '+user_agent)
        request.headers.setdefault('User-Agent', user_agent)
