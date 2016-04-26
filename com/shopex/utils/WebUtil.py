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
    def do_post(url, url_info, params, header_data, is_https=False):
        logger.info("Request Type:do_post \t \n")
        logger.info("Request Url：%s \t \n" % (url))
        logger.info("Request Params:%s \t \n" % (params))
        logger.info("Request Header Message:%s \t \n" % (header_data))

        conn = None
        try:
            params = urllib.urlencode(params)
            if is_https:
                conn = httplib.HTTPSConnection(url_info.host, 443)
            else:
                conn = httplib.HTTPConnection(url_info.host, url_info.port, 30)

            conn.request(METHOD_POST, url, body=params, headers=header_data)
            response = conn.getresponse()
            return response.read()
        except Exception, e:
            logger.error("do_post:%s \t \n" % (e))
        finally:
            if conn:
                conn.close()

    @staticmethod
    def do_get(url, url_info, params, header_data, is_https=False):
        url += WebUtil.build_query(params)
        logger.info("Request Type:do_get \t \n")
        logger.info("Request Url：%s \t \n" % (url))
        logger.info("Request Params:%s \t \n" % (params))
        logger.info("Request Header Message:%s \t \n" % (header_data))
        conn = None
        try:
            if is_https:
                conn = httplib.HTTPSConnection(url_info.host, 443)
            else:
                conn = httplib.HTTPConnection(url_info.host, url_info.port, 30)

            conn.request(METHOD_GET, url, headers=header_data)

            response = conn.getresponse()
            return response.read()
        except Exception, e:
            logger.error("do_get:%s \t \n" % (e))
        finally:
            if conn:
                conn.close()

