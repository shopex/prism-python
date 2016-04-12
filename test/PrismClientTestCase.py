# __author__ = 'daixinyu'
# coding=utf8

import unittest
import json
import struct
import sys
import time
import simplejson

sys.path.append("../")
reload(sys)
sys.setdefaultencoding('utf-8')

from com.shopex.prism.PrismClient import PrismClient


class PrismMessageHandler():
    def __init__(self, sleep=60, retry_times=None):
        self.retry_times = retry_times  # 重试次数,默认断开后一直重试
        self.sleep = sleep  # 间歇时间,默认断开每隔1分钟重试

    # 接受到Websocket服务端信息时触发调用
    def on_message(self, socket, message):
        print "[PrismMessageHandler] socket on_message! \t \n"
        json_message = json.loads(message)
        print "[on_message] %s \t \n" % (json_message)
        # if json_message["tag"] == 1:  # 这里只对第一条消息做ACK应答
        #     print ("[PrismMessageHandler] send ack:%s" % (json_message["tag"]))
        # socket.send(self.assemble_ack_date(json_message["tag"]))

    # def assemble_ack_date(self, tag):
    #     return struct.pack("BB", 0x03, tag + 48)

    def assemble_ack_date(self, tag):
        s = str(tag)
        ret = struct.pack("B", 0x03)
        for i in s:
            print struct.pack("b", ord(i))
            ret = ret + struct.pack("b", ord(i))
        return ret


# data = {
#     "data_type": "zx_order",
#     "datacenter": {
#         "data": "{\"seller_email\": \"\", \"promotion_details\": [], \"tradetype\": \"\", \"is_cod\": \"false\", \"servername\": \"open.shopex.cn\", \"consign_time\": \"\", \"aim_url\": \"http://open.shopex.cn/\", \"point_fee\": \"\", \"currency_rate\": 1.0, \"seller_name\": \"\", \"currency\": \"CNY\", \"buyer_name\": \"\", \"total_weight\": \"\", \"pay_time\": \"2015-10-30 12:51:20\", \"total_currency_fee\": 808.0, \"shipping_type\": \"\", \"receiver_address\": \"龙漕路51弄1号楼104室\", \"has_invoice\": \"true\", \"is_delivery\": \"\", \"orders\": {\"order\": [{\"total_order_fee\": 808.0, \"weight\": \"\", \"title\": \"HUAWEI 荣耀畅玩4X移动高配版 4X联通高配版 双卡双待 4G智能手机 安卓大屏黑色8GB移动高配版CHE-TL10H官方标配\", \"discount_fee\": 0.0, \"type\": \"goods\", \"bn\": \"Y51095427\", \"oid\": 1282299440, \"order_items\": {\"order_item\": [{\"status\": \"active\", \"sku_id\": \"\", \"name\": \"HUAWEI 荣耀畅玩4X移动高配版 4X联通高配版 双卡双待 4G智能手机 安卓大屏黑色8GB移动高配版CHE-TL10H官方标配\", \"sku_properties_string\": \"\", \"item_type\": \"product\", \"discount_fee\": 0.0, \"bn\": \"Y51095427\", \"sku_properties\": \"\", \"total_item_fee\": 808.0, \"weight\": \"\", \"price\": 808.0, \"iid\": 37946912, \"num\": 1, \"sale_price\": 808.0, \"pic_path\": \"\", \"score\": \"\", \"payment\": 808.0, \"sendnum\": \"0\"}]}, \"iid\": 37946912, \"type_alias\": \"商品\", \"sale_price\": 808.0, \"items_num\": 1, \"price\": 808.0}]}, \"trade_memo\": \"\", \"seller_alipay_no\": \"\", \"invoice_desc\": \"\", \"receiver_district\": \"徐汇区\", \"receiver_city\": \"上海市\", \"title\": \"\", \"buyer_message\": \"\", \"orders_discount_fee\": 0.0, \"buyer_memo\": \"\", \"invoice_title\": \"个人(袁金)\", \"receiver_state\": \"上海\", \"aim_node\": \"1281386531\", \"unpaidprice\": 0.0, \"receiver_time\": \"\", \"seller_memo\": \"\", \"protect_fee\": \"\", \"seller_uname\": \"\", \"pay_status\": \"PAY_FINISH\", \"payment_type\": \"网上支付\", \"status\": \"TRADE_ACTIVE\", \"orders_number\": 1, \"total_trade_fee\": 808.0, \"buyer_flag\": \"\", \"pay_cost\": \"\", \"buyer_uname\": \"\", \"commission_fee\": \"\", \"seller_flag\": \"\", \"buyer_email\": \"\", \"trade_discount_fee\": 0.0, \"tid\": \"6183103479704\", \"buyer_alipay_no\": \"\", \"buyer_rate\": \"\", \"receiver_mobile\": \"17092127187\", \"confirm_time\": \"\", \"goods_discount_fee\": 0, \"seller_mobile\": \"\", \"seller_phone\": \"\", \"seller_rate\": \"\", \"shipping_tid\": \"\", \"timeout_action_time\": \"\", \"total_goods_fee\": 808.0, \"created\": \"2015-10-30 10:55:31\", \"discount_fee\": 0.0, \"receiver_phone\": \"\", \"invoice_fee\": \"\", \"modified\": \"2015-10-30 12:52:00\", \"is_protect\": \"\", \"ship_status\": \"SHIP_NO\", \"buyer_obtain_point_fee\": \"\", \"end_time\": \"\", \"payed_fee\": 808.0, \"payment_tid\": 1, \"receiver_name\": \"袁金\", \"shipping_fee\": 0.0, \"alipay_no\": \"\", \"receiver_zip\": \"200030\"}",
#         "lastmodify": "2015-10-30 12:52:00",
#         "order_id": "6183103479704",
#         "order_type": "yihaodian",
#         "type": "prism"
#     },
#     "from_node_id": "1813905234",
#     "from_type": "yihaodian",
#     "msg_id": "5632F7C1C0A81723750E146B66383621",
#     "to_node_id": "1281386531"
# }


class PrismClientTestCase(unittest.TestCase):
    def setUp(self):
        # self.url = 'http://192.168.65.48:8080'
        # self.key = "yjmf3gy3"
        # self.secret = "2ugmc3g4ke5sut64jdk6"
        # self.api = "/api/matrix_api2/"

        # self.url = 'http://7bhjj6wb.apihub.cn'
        # self.key = "3e577wt2"
        # self.secret = "i7ctszkdu75nmsbae5sk"
        # self.api = "/api/matrix_api_jst/"

        # self.url = "http://p26jcsqp.apihub.cn/api"
        # self.key = "zlke7fwm"
        # self.secret = "7vxvrdgxzpilh2ip6ond"
        # self.api = "/api/matrix_api_jst/"

        self.url = "http://omsbbc2.shopexprism.onex.software:8080/api"
        self.key = "5k7y7hnq"
        self.secret = "5ulx44honatwk7rnhnxd"

        self.prismClient = PrismClient(self.url, self.key, self.secret)

        # def testDoGet(self):
        #     params = {'timestamp': '2015-04-15 13:41:27', 'params': '{"status": 0, "from_type": "taobao"}', 'method': 'matrix_item_log_select', 'format': 'json'}
        #     print self.prismClient.do_get('/api/matrix_api/', params)
        #

    # def testDoPost(self):
    #     params = sys_params()
    #     params['method'] = "matrix_prism_queue"
    #     routingkey = "%s.%s.%s" % (1281386531, "yihaodian", "zx_order")
    #     where = {"key": routingkey, "data": data}
    #     params['params'] = simplejson.dumps(where)
    #     response = self.prismClient.do_post(self.api, params)
    #     print response

    def testWebSocketConnect(self):
        method = "/platform/notify"
        queue_name = "messages"
        prism_notify = self.prismClient.notify(method, PrismMessageHandler(sleep=2))
        prism_notify.consume(queue_name)
        # prism_notify.publish("order.new", "mytest00001")


def sys_params():
    params = {
        'timestamp': time.strftime("%Y-%m-%d %H:%M:%S"),
        'format': 'json',
    }
    return params


if __name__ == '__main__':
    unittest.main()
