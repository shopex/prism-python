# __author__ = 'daixinyu'
# coding=utf8
import urllib
import urlparse


class UrlParser():
    def __init__(self, url):
        parsed_tuple = urlparse.urlparse(url)
        self.protocol, self.rest = urllib.splittype(url)
        self.host, self.rest = urllib.splithost(self.rest)
        self.host, self.port = urllib.splitport(self.host)
        if self.port is None:
            self.port = 80
        self.path = parsed_tuple.path
        self.query = parsed_tuple.query

    def get_site(self):
        return self.protocol + "://" + self.host + ("" if self.port == 80 else ":" + self.port)

    def get_site_path(self, path):
        return self.get_site() + path

    def get_site_with_path(self):
        return self.get_site() + self.path

    def get_site_with_append_path(self, append_path):
        return self.get_site_with_path() + append_path

    def get_full_url(self):
        full_url = self.get_site_with_path()
        if self.query:
            return full_url + "?" + self.query
        return full_url

    def get_ws_url(self, method):
        return "ws://" + self.host + ("" if self.port == 80 else ":" + self.port) + self.path + method

    def get_ws_path(self, method):
        return self.path + method

