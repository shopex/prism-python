# __author__ = 'daixinyu'
# coding=utf8
from com.shopex import websocket

from com.shopex.utils.LogUtil import logger
# from com.shopex.prism.MessageHandler import PrismMessageHandler
from com.shopex.websocket import ABNF
import struct

# websocket.enableTrace(True)

class PrismNotify():
    # socket
    def __init__(self, ws_url, message_handler):
        # PrismMessageHandler.__init__(self)
        self.socket = websocket.WebSocketApp(ws_url,
                                             on_message=message_handler.on_message,
                                             on_error=message_handler.on_error,
                                             on_close=message_handler.on_close)
        self.data = None

    def on_open(self, ws):
        logger.info("[PrismNotify] on_open %s " %(self.data))
        ws.send(self.data)
        # ws.send(self.data, opcode=ABNF.OPCODE_BINARY)

    # 组装发布消息
    def publish(self, routing_key, message):
        logger.info("[PrismNotify] publish")
        self.data = self.assemble_publish_data(routing_key, message)
        self.socket.on_open = self.on_open
        self.socket.run_forever()

    # 消费信息
    def consume(self):
        logger.info("[PrismNotify] consume")
        self.data = self.assemble_consume_date()
        self.socket.on_open = self.on_open
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


    def assemble_consume_date(self):
        return struct.pack("B", 0x02)

