# coding: utf-8
import json
import os
import sys
from collections import OrderedDict

import pymongo

PROJ_HOME = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJ_HOME)

from lagou.settings import MONGO_URI, MONGO_DATABASE, COLLECTION_NAME
"""
For the analyzing of captured job data.
"""


def keywords_stats(conn):
    # ret = conn.find({'job_id': {'$lt': '500478'}}, {'tech_keywords': 1, '_id': 0})
    ret = conn.find({}, {'tech_keywords': 1, '_id': 0})
    stats_result = clean_keywords(ret)
    print json.dumps(stats_result)


def clean_keywords(data):
    result = {}
    for item in data:
        for keyword in item['tech_keywords']:
            if '/' in keyword and keyword != 'tcp/ip':
                words = keyword.split('/')
                for x in words:
                    result[x] = result.setdefault(x, 0) + 1
            else:
                result[keyword] = result.setdefault(keyword, 0) + 1
    result = OrderedDict(sorted(result.iteritems(), key=lambda d: d[1], reverse=True))
    return result


def job_requests_stats(conn):
    ret = conn.find({}, {'job_requests': 1, '_id': 0})
    stats_result = clean_job_requests(ret)
    print json.dumps(stats_result)


def clean_job_requests(data):
    salary, location, experience, degree, type_ = {}, {}, {}, {}, {}

    for item in data:
        sal = salary_average(item['job_requests'][0].encode('utf-8'))
        salary[sal] = salary.setdefault(sal, 0) + 1
        # loc = item['job_requests'][1]
        # location[loc] = location.setdefault(loc, 0) + 1
        # exp = item['job_requests'][2]
        # experience[exp] = experience.setdefault(exp, 0) + 1
        # deg = item['job_requests'][3]
        # degree[deg] = degree.setdefault(deg, 0) + 1
        # typ = item['job_requests'][4]
        # type_[typ] = type_.setdefault(typ, 0) + 1

    result = {
        'salary': salary,
        # 'location': location,
        # 'experience': experience,
        # 'degree': degree,
        # 'type': type_
    }
    return result


def salary_average(salary_range):
    if '-' in salary_range:
        lower, upper = salary_range.split('-')
        return sum([int(lower[:-1]), int(upper[:-1])])/2
    else:
        return int(salary_range.split('k')[0])


class MongoManager(object):

    _client = pymongo.MongoClient(MONGO_URI)

    @classmethod
    def init_connection(cls, db=MONGO_DATABASE, collection=COLLECTION_NAME):
        db = cls._client[MONGO_DATABASE]
        collection = db[COLLECTION_NAME]
        return collection

    @classmethod
    def close_connection(cls):
        cls._client.close()


def main():
    conn = MongoManager.init_connection()
    # keywords_stats(conn)
    job_requests_stats(conn)

if __name__ == '__main__':
    main()
