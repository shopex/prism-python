# __author__ = 'daixinyu'
# coding=utf8

from com.shopex.python.prism.PrismClient import PrismClient


class PrismOauth(PrismClient):
    def __init__(self, url, key, secret):
        PrismClient.__init__(url, key, secret)

    def require_oauth(self):
        self.token
