# __author__ = 'daixinyu'
#coding=utf8

from com.shopex.python.utils.UrlParser import UrlParser

if __name__ == '__main__':
    urlParser = UrlParser("http://www.google.com/search?hl=en&q=urlparse&btnG=Google+Search")
    print ("%s \n") % (urlParser.protocol)
    print ("%s \n") % (urlParser.rest)
    print ("%s \n") % (urlParser.host)
    print ("%s \n") % (urlParser.port)
    print ("%s \n") % (urlParser.path)
    print ("%s \n") % (urlParser.query)
    print ("%s \n") %(urlParser.get_site())
