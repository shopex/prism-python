# __author__ = 'daixinyu'
# coding=utf8

from com.shopex.utils.LogUtil import logger
from com.shopex.prism.PrismMessage import PrismMessage


class PrismMessageHandler():
    def __init__(self):
        pass


    def on_message(self, socket, message):
        logger.info("[PrismMessageHandler] socket on_message!message is %s \t \n" % (message))
        prism_message = PrismMessage()
        socket.send(prism_message.assemble_ack_date())
        logger.info("[PrismNotify] send ack:%s" % (message.tag_id))

    def on_close(self, socket):
        logger.info("[PrismMessageHandler] on_close")

    def on_error(self, socket):
        logger.info("[PrismMessageHandler] on_error")
