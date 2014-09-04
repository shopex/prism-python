# __author__ = 'daixinyu'
# coding=utf8
import urllib
import httplib

from com.shopex.utils.LogUtil import logger
from com.shopex.config import *


class WebUtil():
    def __init__(self):
        pass

    @staticmethod
    def build_query(params={}):
        query = "?"
        if not params:
            return ""
        for key, val in params.iteritems():
            query += key + "=" + str(val) + "&"
        return query[0:len(query) - 1]


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
            conn.request(METHOD_POST, url, body=params, headers=header_data)
            response = conn.getresponse()
            return response.read()
        except Exception, e:
            print e
        finally:
            if conn:
                conn.close()

    @staticmethod
    def do_get(url, url_info, params, header_data):
        url += WebUtil.build_query(params)
        logger.info("请求方式:do_get \t \n")
        logger.info("请求url：%s \t \n" % (url))
        logger.info("请求参数:%s \t \n" % (params))
        logger.info("请求头消息:%s \t \n" % (header_data))

        conn = None
        try:
            conn = httplib.HTTPConnection(url_info.host, url_info.port)
            conn.request(METHOD_GET, url, headers=header_data)

            response = conn.getresponse()
            return response.read()
        except Exception, e:
            print e
        finally:
            if conn:
                conn.close()

