# coding: utf-8
import json
from collections import OrderedDict

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


def wirte_json_file(data, file_name, folder='./data/', mode='w'):
    with open(folder+file_name, mode) as f:
        json.dump(data, f)


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
