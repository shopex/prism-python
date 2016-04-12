# __author__ = 'daixinyu'
# coding=utf8
from com.shopex import websocket

from com.shopex.utils.LogUtil import logger
import struct, time

# websocket.enableTrace(True)

class PrismNotify():
    # socket
    def __init__(self, ws_url, message_handler):
        self.ws_url = ws_url
        self.message_handler = message_handler
        self.retry_times = message_handler.retry_times
        self.sleep = message_handler.sleep
        self.real_times = 0
        self.socket = websocket.WebSocketApp(self.ws_url,
                                             on_open=self.on_open,
                                             on_message=self.message_handler.on_message,
                                             on_error=self.on_error,
                                             on_close=self.on_close)
        self.data = None

    def on_open(self, ws):
        logger.info("[PrismNotify] on_open %s " % (self.data))
        ws.send(self.data)

    # Websocket连接关闭时触发调用
    def on_close(self, socket):
        logger.info("[PrismNotify] on_close")
        logger.info("[PrismNotify] real_times:%s \t retry_times:%s \t \n" % (self.real_times, self.retry_times))
        if self.real_times < self.retry_times or self.retry_times == None:
            time.sleep(self.sleep)
            self.socket = websocket.WebSocketApp(self.ws_url,
                                                 on_open=self.on_open,
                                                 on_message=self.message_handler.on_message,
                                                 on_error=self.on_error,
                                                 on_close=self.on_close)
            self.consume()

    # Websocket发生异常时触发调用
    def on_error(self, socket, error):
        logger.info("[PrismNotify] on_error,error is %s" % (error))

    # 组装发布消息
    def publish(self, routing_key, message):
        logger.info("[PrismNotify] publish")
        self.data = self.assemble_publish_data(routing_key, message)
        self.socket.run_forever()

    # 消费信息
    def consume(self, queuq_name):
        self.real_times += 1
        logger.info("[PrismNotify] consume")
        self.data = self.assemble_consume_date(queuq_name)
        self.socket.run_forever()

    # 封装消息
    def assemble_publish_data(self, routing_key, message, content_type="text/plain"):
        routing_key_pack = struct.pack(">H%ds" % len(routing_key), 2, routing_key)
        message_pack = struct.pack(">I%ds" % len(message), 4, message)
        content_type_pack = struct.pack(">H%ds" % len(content_type), 2, content_type)

        content_pack = struct.pack("%ds%ds%ds" % (len(routing_key_pack), len(message_pack), len(content_type_pack)),
                                   routing_key_pack, message_pack, content_type_pack)
        return struct.pack("B%ds" % (len(content_pack)), 0x01, content_pack)

    def assemble_ack_date(self, tag):
        return struct.pack("BB", 0x03, tag + 48)

    def assemble_consume_date(self, queuq_name):
        if len(queuq_name) > 0:
            ret = struct.pack("BBB", 0x02, len(queuq_name) / 256, len(queuq_name) % 256)
            for i in queuq_name:
                ret = ret + struct.pack('s', i)
            return ret
        else:
            return struct.pack("B", 0x02)
