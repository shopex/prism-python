# __author__ = 'daixinyu'
# coding=utf8

import unittest
import json
import struct
import sys
sys.path.append("../")
reload(sys)
sys.setdefaultencoding('utf-8')

from com.shopex.prism.PrismClient import PrismClient


class PrismMessageHandler():
    def __init__(self, sleep=60, retry_times=None):
        self.retry_times = retry_times   #重试次数,默认断开后一直重试
        self.sleep = sleep               #间歇时间,默认断开每隔1分钟重试

    # 接受到Websocket服务端信息时触发调用
    def on_message(self, socket, message):
        print "[PrismMessageHandler] socket on_message! \t \n"
        json_message = json.loads(message)
        # print "[on_message] %s \t \n" % (json_message)
        # if json_message["tag"] == 1:  # 这里只对第一条消息做ACK应答
        #     print ("[PrismMessageHandler] send ack:%s" % (json_message["tag"]))
        socket.send(self.assemble_ack_date(json_message["tag"]))

    # def assemble_ack_date(self, tag):
    #     return struct.pack("BB", 0x03, tag + 48)

    def assemble_ack_date(self,tag):
        s = str(tag)
        ret = struct.pack("B", 0x03)
        for i in s:
            print struct.pack("b", ord(i))
            ret = ret + struct.pack("b", ord(i))
        return ret


class PrismClientTestCase(unittest.TestCase):
    def setUp(self):
        self.url = 'http://192.168.65.48/api'
        self.key = "7wl3rb4q"
        self.secret = "hjcajuiegtwsktcufj6x"

        # self.url = 'http://p26jcsqp.apihub.cn/api'
        # self.key = "zlke7fwm"
        # self.secret = "7vxvrdgxzpilh2ip6ond"
        self.prismClient = PrismClient(self.url, self.key, self.secret)

    # def testDoGet(self):
    #     params = {'timestamp': '2015-04-15 13:41:27', 'params': '{"status": 0, "from_type": "taobao"}', 'method': 'matrix_item_log_select', 'format': 'json'}
    #     print self.prismClient.do_get('/api/matrix_api/', params)
    #
    # def testDoPost(self):
    #     params = {}
    #     print self.prismClient.do_post("/api/platform/notify/status", params)

    def testWebSocketConnect(self):
        method = "/platform/notify"
        prism_notify = self.prismClient.notify(method, PrismMessageHandler(sleep=2))
        prism_notify.consume()
        # prism_notify.publish("order.new", "mytest00001")


if __name__ == '__main__':
    unittest.main()
