# __author__ = 'daixinyu'
# coding=utf8
import web

from com.shopex.prism.PrismOauth import PrismOauth

from com.shopex.utils.LogUtil import path


class LoginHandler():
    def __init__(self):
        self.url = "http://dilbmtcv.apihub.cn/api"
        self.key = "buwb2lii"
        self.secret = "ucr72ygfutspqeuu6s36"

    def GET(self):
        prism_oauth = PrismOauth(self.url, self.key, self.secret, session)
        prism_oauth.require_oauth()
        return "Hello PrismOauth"


# web.config.debug = True

urls = (
    "/user/login*", "LoginHandler")
app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore(path + "sessions"), initializer={})


def start_up():
    app.run()


if __name__ == "__main__":
    start_up()


