# coding: utf-8
import logging

# roledefs = {
#     'local_test': ['root@192.168.1.114:22', ],
#     'production': ['10.19.54.11', '10.19.54.12'],
#     'gray': ['bndk@10.19.54.13:22', ]
# }

# passwords = {
#     'root@192.168.1.114:22': '123321',
# }

hosts = ['107.170.207.236:23334']
user = 'redev'
key_filename = 'C:\Users\Administrator\.ssh\do1.pem'


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