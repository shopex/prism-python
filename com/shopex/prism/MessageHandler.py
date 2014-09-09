# __author__ = 'daixinyu'
# coding=utf8

import json
import struct

from com.shopex.utils.LogUtil import logger


class PrismMessageHandler():
    def __init__(self):
        pass

    def on_message(self, socket, message):
        logger.info("[PrismMessageHandler] socket on_message!message is %s \t \n" % (message))
        json_message = json.loads(message)
        if json_message["tag"] == 1:
            logger.info("[PrismNotify] send ack:%s" % (json_message["tag"]))
            socket.send(self.assemble_ack_date(json_message["tag"]))

    def on_close(self, socket):
        logger.info("[PrismMessageHandler] on_close")

    def on_error(self, socket):
        logger.info("[PrismMessageHandler] on_error")

    # 封装消息
    def assemble_publish_data(self, routing_key, message, content_type="text/plain"):
        format = "ii%dsi%dsi%ds" % (len(routing_key), len(message), len(content_type))
        return struct.pack(format, 0x01, 2, routing_key, 4, message, 4, content_type)

    def assemble_ack_date(self, tag):
        return struct.pack("ii", 0x03, tag + 48)

    def assemble_consume_date(self):
        return struct.pack("h", 0x02)
