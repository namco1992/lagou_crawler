# coding: utf-8
import json
import os
import sys

PROJ_HOME = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJ_HOME)

from settings import OMITTING_WORDS
from utils import count_filter, MongoManager, dict_sort, wirte_json_file
"""
For the analyzing of captured job data.
"""


def keywords_stats(conn):
    # ret = conn.find({'job_id': {'$lt': '500478'}}, {'tech_keywords': 1, '_id': 0})
    ret = conn.find({}, {'tech_keywords': 1, '_id': 0})
    stats_result = clean_keywords_v2(ret)
    wirte_json_file(stats_result, 'keywords_stats.json')


def clean_keywords(data):
    result = {}
    for item in data:
        for keyword in item['tech_keywords']:
            if '/' in keyword and keyword != 'tcp/ip':
                words = keyword.split('/')
                for x in words:
                    x = x.strip()
                    if x not in OMITTING_WORDS and len(x) > 0:
                        result[x] = result.setdefault(x, 0) + 1
            elif keyword not in OMITTING_WORDS:
                result[keyword] = result.setdefault(keyword, 0) + 1
    result = count_filter(result, 100)
    return dict_sort(result)


def clean_keywords_v2(data):
    result = {}
    prepared_data = {'keywords': [], 'counts': []}
    for item in data:
        for keyword in item['tech_keywords']:
            if '/' in keyword and keyword != 'tcp/ip':
                words = keyword.split('/')
                for x in words:
                    x = x.strip()
                    if x not in OMITTING_WORDS and len(x) > 0:
                        result[x] = result.setdefault(x, 0) + 1
            elif keyword not in OMITTING_WORDS:
                result[keyword] = result.setdefault(keyword, 0) + 1
    result = dict_sort(count_filter(result, 100))
    for key, value in result.iteritems():
        prepared_data['keywords'].append(key)
        prepared_data['counts'].append(value)
    # return dict_sort(result)
    return prepared_data


def job_requests_stats(conn):
    ret = conn.find({}, {'job_requests': 1, '_id': 0})
    stats_result = clean_job_requests(ret)
    for item, data in stats_result.iteritems():
        wirte_json_file(data, item+'.json')


def clean_job_requests(data):
    salary, location, experience, degree, type_ = {}, {}, {}, {}, {}

    for item in data:
        sal = salary_average(item['job_requests'][0])
        salary[sal] = salary.setdefault(sal, 0) + 1
        loc = item['job_requests'][1]
        location[loc] = location.setdefault(loc, 0) + 1
        exp = item['job_requests'][2]
        experience[exp] = experience.setdefault(exp, 0) + 1
        deg = item['job_requests'][3]
        degree[deg] = degree.setdefault(deg, 0) + 1
        typ = item['job_requests'][4]
        type_[typ] = type_.setdefault(typ, 0) + 1

    # generate salary stats for pie chart
    # clean experience data
    experience = dict_sort(count_filter(experience, 10))
    # clean location data
    location = dict_sort(count_filter(location, 30))
    # generate result
    result = {
        'salary': salary,
        'location': location,
        'experience': experience,
        'degree': degree,
        'type': type_
    }

    return result


def salary_average(salary_range):
    if '-' in salary_range:
        lower, upper = salary_range.split('-')
        return sum([int(lower[:-1]), int(upper[:-1])]) / 2
    else:
        return int(salary_range.split('k')[0])


def main():
    conn = MongoManager.init_connection()
    keywords_stats(conn)
    # job_requests_stats(conn)
    MongoManager.close_connection()

if __name__ == '__main__':
    main()
