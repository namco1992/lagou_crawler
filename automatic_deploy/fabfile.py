# coding: utf-8
import os
import sys

from fabric.api import *
from fabric.colors import green, red

# append the home path
PROJECT_HOME = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(PROJECT_HOME)

from settings import (
    hosts, user, key_filename, DirConfig as DC)
from utils import init_logging_handler, timestamp

env.hosts, env.user, env.key_filename = hosts, user, key_filename

logger = init_logging_handler()


def prepare_deploy():
    with lcd(DC.ANALYSIS_DIR):
        local("ipython analyze.py")


def zip_files():
    with lcd(DC.LOCAL_RELATIVE_DATA_DIR+'data_'+timestamp()):
        local('tar -czf data.tar.gz ./')
        local('mv data.tar.gz ../../automatic_deploy/deploy_files')


def upload():
    # upload the zipped files
    with lcd(DC.LOCAL_TAR_DIR):
        put('data.tar.gz', DC.REMOTE_BASE_DIR+'data.tar.gz')


def deploy():
    with cd(DC.REMOTE_BASE_DIR):
        run('tar -xvzf data.tar.gz -C %s' % DC.REMOTE_PROJ_DIR)


def test():
    with settings(warn_only=False):
        prepare_deploy()
        zip_files()
        upload()
        deploy()
