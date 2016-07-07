# coding: utf-8
import logging

hosts = ['192.168.1.1:22']
user = 'example_user'
key_filename = 'path/to/pem'


class LogConfig(object):
    LOGGING_FORMAT = '%(asctime)s %(funcName)s:%(lineno)d [%(levelname)s] %(message)s'
    LOGGING_LOCATION = './log/automatic_deploy.log'
    LOGGING_LEVEL = logging.DEBUG


class DirConfig(object):
    REMOTE_BASE_DIR = './deploy/'
    REMOTE_PROJ_DIR = 'job_analysis/app/static/data'
    LOCAL_RELATIVE_DATA_DIR = '../data/'
    LOCAL_TAR_DIR = 'deploy_files/'
    ANALYSIS_DIR = '../analysis'
