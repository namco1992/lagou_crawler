# coding: utf-8
import logging
import re

from scrapy import signals


class ExtensionForItemStats(object):

    def __init__(self, stats):
        self.stats = stats

    @classmethod
    def from_crawler(cls, crawler):
        ext = cls(crawler.stats)
        crawler.signals.connect(ext.item_scraped, signal=signals.item_scraped)
        return ext

    def item_scraped(self, item, spider):
        # 需要在这里执行较为复杂的逻辑
        # 目前尚不清楚对性能的影响
        # 清洗数据
        # job_desc = re.sub(r'</?\w+[^>]*>|\s', '', item['job_desc'])
        # required_list = []
        # for desc in item['job_desc']:
        #     keywords = re.findall(ur'[a-zA-Z/\s]{2,}', desc)
        #     if len(keywords) > 0:
        #         required_list.extend((x.strip() for x in keywords))
        # required_list = set(required_list)
        # item['tech_keywords'] = set(required_list)
        # logging.info('=======required_list: %s', item['tech_keywords'])
        # 计数
        for i in item['tech_keywords']:
            self.stats.inc_value(i.lower().strip())
        logging.info('=======STATS: %s', self.stats.get_stats())


if __name__ == '__main__':
    item = {
    "_id" : "56839b92f76f330c54cd0aec",
    "keywords" : "<meta content=\"Python,Python招聘,广州灵酷企业服务有限公司Python招聘\" name=\"keywords\">",
    "job_id" : 1.30065e+006,
    "job_desc" : "<dd class=\"job_bt\">\n        <h3 class=\"description\">职位描述</h3>\n    python web    <p>一：工作内容：</p>\n<p>1、全球出口电商平台（ebay、速卖通、wish）等平台数据抓取<br></p>\n<p>2、协助开发公司BI商业智能系统的开发<br></p>\n<p>3、与数据挖掘部门同事配合，实现数据获取到挖掘的高效对接<br></p>\n<p><br></p>\n<p>二：职位要求</p>\n<p>1、1年以上爬虫相关工作经验</p>\n<p>2、熟悉基于正则表达式、CSS、http协议，xml等的网页信息抽取技术（解析，dom数， xpath）<br></p>\n<p>3、熟悉多线程、多进程、网络通信编程相关知识<br></p>\n<p>4：具备独立开发的态度，与业务部门保持高效沟通</p>\n<p><br></p>\n<p>三：公司介绍<br></p>\n<p> 1：广州灵酷隶属于百伦集团，是一家专业化从事跨境电子商务的专业化服务机构，年营业额超3亿元人民币，公司目前已完成A轮投资，预计2016年即可完成IPO上市。旗下拥有跨境出口业务，全球物流仓储业务，全球税务法务知识产权服务，供应链金融服务，灵酷跨境进口业务。</p>\n<p>2：核心团队：核心团队均具备5年以上的电子商务实操经验，IT部组成人员包含BAT3家中的技术专家，且拥有全球物流仓储、全球税务法务知识产权、全球采购等方面的专家</p>\n<p><br></p>\n    </dd>"
    }
    job_desc = re.sub(r'</?\w+[^>]*>|\s', '', item['job_desc'])
    print job_desc
    required_list = re.findall(r'[a-zA-Z\s ]+', job_desc)
    print required_list