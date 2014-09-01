# __author__ = 'daixinyu'
# coding=utf8
import web


class LoginHandler():
    def __init__(self):
        pass

    def GET(self, action):
        i = web.input()
        print action, i
        referer = web.ctx.env.get('HTTP_REFERER', 'http://www.baidu.com?1=1')
        web.header('Content-Type', 'text/html; charset=UTF-8')
        return web.seeother(referer)