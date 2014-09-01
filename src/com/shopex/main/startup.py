# __author__ = 'daixinyu'
# coding=utf8
import web
from com.shopex.python.handler.LoginHandler import LoginHandler

web.config.debug = True
urls = (
    '/user/login/(.*)', 'LoginHandler')
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
