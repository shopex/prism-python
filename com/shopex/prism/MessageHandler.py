# __author__ = 'daixinyu'
# coding=utf8

from com.shopex.utils.LogUtil import logger


class PrismMessageHandler():
    def __init__(self):
        pass

    def on_open(self, socket):
        logger.info("[PrismMessageHandler] on_open")

    def on_message(self, socket, message):
        logger.info("[PrismMessageHandler] socket on_message")
        if message.tag_id == 1:
            # socket.send("ack_data")
            logger.info("[PrismNotify] send ack:%s" % (message.tag_id))

    def on_close(self, socket):
        logger.info("[PrismMessageHandler] on_close")

    def on_error(self, socket):
        logger.info("[PrismMessageHandler] on_error")
