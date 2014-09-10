# __author__ = 'daixinyu'
# coding=utf8
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

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
        routing_key_pack = struct.pack(">H%ds" % len(routing_key), 2, routing_key)
        message_pack = struct.pack(">I%ds" % len(message), 4, message)
        content_type_pack = struct.pack(">H%ds" % len(content_type), 2, content_type)

        content_pack = struct.pack("%ds%ds%ds" % (len(routing_key_pack), len(message_pack), len(content_type_pack)), routing_key_pack, message_pack,content_type_pack)
        return struct.pack("B%ds" % (len(content_pack)), 0x01, content_pack)


    def assemble_ack_date(self, tag):
        return struct.pack("BB", 0x03, tag + 48)


    def assemble_consume_date(self):
        return struct.pack("B", 0x02)
