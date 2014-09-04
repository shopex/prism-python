# __author__ = 'daixinyu'
# coding=utf8
import logging
import sys
import os
import time

PROJECT_NAME = u'prism-python'
path = os.getcwdu()
path = path[:path.find(PROJECT_NAME) + len(PROJECT_NAME)] + os.path.sep

logger = logging.getLogger("prism-python-sdk")

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
if not os.path.isdir(path + "log"):
    os.makedirs(path + "log")
log_file_path = path + "log" + os.path.sep + "log%s.log" % (time.strftime("%Y%m%d"))
file_handler = logging.FileHandler(log_file_path)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler(sys.stderr)
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

logger.setLevel(logging.DEBUG)
