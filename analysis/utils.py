# coding: utf-8
import json
import os
from collections import OrderedDict
from datetime import date

import pymongo

from settings import LOCAL_URI, MONGO_DATABASE, COLLECTION_NAME


def count_filter(data, threshold):
    result = {}
    for item, count in data.iteritems():
        if count > threshold:
            result[item] = count
    return result


def dict_sort(data, reverse=True):
    return OrderedDict(sorted(data.iteritems(), key=lambda d: d[1], reverse=reverse))


def wirte_json_file(data, file_name, folder='../data/', mode='w', seperate_by_date=True):
    if seperate_by_date:
        folder += 'data_%s/' % timestamp()
        if not os.path.exists(folder):
            os.mkdir(folder)
    with open(folder+file_name, mode) as f:
        json.dump(data, f)


def timestamp():
    return date.today().strftime('%Y%m%d')


def _generate_section_sum(data, lower=0, upper=100000):
    return sum([y for x, y in data.iteritems() if lower <= int(x) <= upper])


class MongoManager(object):

    _client = pymongo.MongoClient(LOCAL_URI)

    @classmethod
    def init_connection(cls, db=MONGO_DATABASE, collection=COLLECTION_NAME):
        db = cls._client[MONGO_DATABASE]
        collection = db[COLLECTION_NAME]
        return collection

    @classmethod
    def close_connection(cls):
        cls._client.close()


if __name__ == '__main__':
    print timestamp()
