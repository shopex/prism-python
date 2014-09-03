# __author__ = 'daixinyu'
# coding=utf8

from com.shopex.python.prism.PrismClient import PrismClient
import web
from com.shopex.python.utils.SignTools import *
from com.shopex.python.utils.WebUtil import WebUtil
import json
from com.shopex.python.utils.LogUtil import logger


class PrismOauth(PrismClient):
    def __init__(self, url, key, secret, session):
        PrismClient.__init__(self, url, key, secret)
        self.session = session

    def require_oauth(self):
        code = self.get_params("code")
        if not isBlank(code):
            self.go_token(code)
            return

        prism_session_id = self.get_session("session_id")
        if not prism_session_id:
            self.go_authorize()
            return

        if not self.check_session_id(prism_session_id):
            self.go_authorize()
            return

    def check_session_id(self, prism_session_id):
        session_params = {"session_id": prism_session_id}
        result = self.do_post(self.check_session_url, session_params)
        logger.info("[check_session_id] %s \t \n" % (result))
        return True

    # 获取令牌
    def go_token(self, code):
        token_params = {"code": code, "grant_type": "authorization_code", "client_id": self.key, "client_secret": self.secret, "state": "1212"}
        result = WebUtil.do_post(self.token_url, self.url_info, token_params, self.get_headers())
        logger.info("[go_token] %s \t \n" % (result))
        # todo
        token_result = json.loads('{"access_token":"1", "session_id":"2","refresh_token":"3"}')
        self.token = token_result["access_token"]
        self.session_id = token_result["session_id"]
        self.refresh_token = token_result["refresh_token"]
        if not isBlank(self.token):
            self.set_session("session_id", self.session_id)

    # 获取临时访问令牌
    def go_authorize(self):
        oauth_params = {"state": 1212, "client_id": self.key, "redirect_uri": "http://" + web.ctx.host + web.ctx.path, "response_type": "code"}
        query = WebUtil.build_query(params=oauth_params)
        if query:
            # web.seeother(self.authorize_url + "?" + query)
            web.redirect(self.authorize_url + "?" + query)

    def get_params(self, s):
        i = web.input()
        try:
            return i[s]
        except Exception, e:
            return None

    def get_session(self, s):
        try:
            return self.session._initializer[s]
        except Exception, e:
            return ""

    def set_session(self, name, val):
        self.session._initializer[name] = val



