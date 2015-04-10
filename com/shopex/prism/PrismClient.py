# __author__ = 'daixinyu'
# coding=utf8
import hashlib
import time

from com.shopex.utils.UrlParser import UrlParser

from com.shopex.prism.PrismNotify import PrismNotify
from com.shopex.utils.SignTools import *
from com.shopex.utils.WebUtil import *
from com.shopex import websocket


class PrismClient:
    def __init__(self, url, key, secret):
        self.url = url
        self.key = key
        self.secret = secret
        self.url_info = UrlParser(self.url)
        self.token_url = self.url_info.get_site_path("/oauth/token")
        self.authorize_url = self.url_info.get_site_path("/oauth/authorize")
        self.check_session_url = self.url_info.get_site_with_append_path("/platform/oauth/session_check")
        self.sys_params = {}
        self.token = ""
        self.session_id = ""
        self.refresh_token = ""
        self.init_sys_params()

    def notify(self, method, message_handler):
        ws_url = self.url_info.get_ws_url(method) + WebUtil.build_query(self.fix_params(None, {}, METHOD_GET, self.url_info.get_ws_path(method)))
        # ws_url = "ws://echo.websocket.org/"
        return PrismNotify(ws_url, message_handler)

    def init_sys_params(self):
        self.sys_params[CLIENT_ID] = self.key
        self.sys_params[SIGN_METHOD] = "md5"
        self.sys_params[SIGN_TIME] = int(time.time())

    def do_post(self, action, params):
        url_str = self.url_info.get_site_with_append_path(action)
        is_https = True if self.url_info.protocol == "https" else False
        return WebUtil.do_post(url_str, self.url_info,
                               self.fix_params(self.get_headers(), params, METHOD_POST, UrlParser(url_str).path), self.get_headers(),
                               is_https=is_https)

    def do_get(self, action, params):
        url_str = self.url_info.get_site_with_append_path(action)
        is_https = True if self.url_info.protocol == "https" else False
        return WebUtil.do_get(url_str, self.url_info, self.fix_params(self.get_headers(), params, METHOD_GET, UrlParser(url_str).path), self.get_headers(),
                              is_https=is_https)

    def fix_params(self, headers, params, method, url_path):
        all_params = dict(params.items() + self.sys_params.items())
        if self.url_info.protocol == "https":
            all_params["client_secret"] = self.secret

        if method == METHOD_GET:
            all_params[SIGN] = self.sign(headers, all_params, "", METHOD_GET, url_path)
        elif method == METHOD_POST:
            all_params[SIGN] = self.sign(headers, "", all_params, METHOD_POST, url_path)
        return all_params

    def sign(self, headers, get_params, post_params, method_type, url_path):
        md5 = hashlib.md5()
        str_header = mix_header_params(headers)
        str_get_param = mix_request_params(get_params)
        str_post_param = mix_request_params(post_params)
        mix_all_params = self.secret + SEPARATOR + method_type + SEPARATOR + url_encode(url_path) \
                         + SEPARATOR + urllib.quote(str_header, safe='') + SEPARATOR + urllib.quote(str_get_param, safe='') \
                         + SEPARATOR + urllib.quote(str_post_param, safe='') + SEPARATOR + self.secret

        logger.info("[sign]%s \t \n" % (mix_all_params))
        md5.update(mix_all_params)
        md5.digest()
        return md5.hexdigest().upper()

    def get_headers(self):
        headers = {"User-Agent": "PrismSDK/PYTHON", "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}
        if self.token:
            headers["Authorization"] = self.token
        return headers