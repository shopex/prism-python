# __author__ = 'daixinyu'
# coding=utf8
import web

from com.shopex.python.utils.LogUtil import path

# web.config.debug = True
urls = (
    "/user/login*", "LoginHandler")
app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore(path + "sessions"), initializer={})

if __name__ == "__main__":
    app.run()

from com.shopex.python.prism.PrismOauth import PrismOauth


class LoginHandler():
    def __init__(self):
        self.url = "http://dilbmtcv.apihub.cn/api"
        self.key = "buwb2lii"
        self.secret = "ucr72ygfutspqeuu6s36"

    def GET(self):
        prism_oauth = PrismOauth(self.url, self.key, self.secret, session)
        prism_oauth.require_oauth()
        return "Hello PrismOauth"