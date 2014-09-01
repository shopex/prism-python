# __author__ = 'daixinyu'
# coding=utf8
import urllib
import httplib

from com.shopex.python.config.config import *
from com.shopex.python.utils.LogUtil import logger


class WebUtil():
    def __init__(self):
        pass

    @staticmethod
    def do_post(url, url_info, params, header_data):
        logger.info("请求方式:do_post \t \n")
        logger.info("请求url：%s \t \n" % (url))
        logger.info("请求参数:%s \t \n" % (params))
        logger.info("请求头消息:%s \t \n" % (header_data))

        conn = None
        try:
            params = urllib.urlencode(params)
            conn = httplib.HTTPConnection(url_info.host, url_info.port)
            conn.request(method=METHOD_POST, url=url, body=params, headers=header_data)
            response = conn.getresponse()
            return response.read()
        except Exception, e:
            print e
        finally:
            if conn:
                conn.close()

    @staticmethod
    def do_get(url, url_info, params, header_data):
        logger.info("请求方式:do_get \t \n")
        logger.info("请求url：%s \t \n" % (url))
        logger.info("请求参数:%s \t \n" % (params))
        logger.info("请求头消息:%s \t \n" % (header_data))

        conn = None
        try:
            params = urllib.urlencode(params)
            conn = httplib.HTTPConnection(url_info.host, url_info.port)
            conn.request(method=METHOD_GET, url=url, body=params, headers=header_data)

            response = conn.getresponse()
            return response.read()
        except Exception, e:
            print e
        finally:
            if conn:
                conn.close()

