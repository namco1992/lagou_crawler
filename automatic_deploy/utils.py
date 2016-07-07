# coding: utf8
import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import date

from settings import LogConfig as LC


def init_logging_handler():
    handler = TimedRotatingFileHandler(LC.LOGGING_LOCATION, when='MIDNIGHT')
    # handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter(LC.LOGGING_FORMAT)
    handler.setFormatter(formatter)
    logger = logging.getLogger("fabric")
    logger.setLevel(LC.LOGGING_LEVEL)
    logger.addHandler(handler)
    return logger


def timestamp():
    return date.today().strftime('%Y%m%d')


def generate_filename():
    pass


if __name__ == '__main__':
    print timestamp()
