# __author__ = 'daixinyu'
# coding=utf8
from com.shopex import websocket

from com.shopex.prism.PrismMessage import PrismMessage
from com.shopex.utils.LogUtil import logger
from com.shopex.prism.MessageHandler import PrismMessageHandler

# websocket.enableTrace(True)


class PrismNotify(PrismMessageHandler):
    # socket
    def __init__(self, ws_url):
        PrismMessageHandler.__init__(self)
        self.socket = websocket.WebSocketApp(ws_url,
                                             on_message=self.on_message,
                                             on_error=self.on_error,
                                             on_close=self.on_close)
        self.message = ""

    def on_open(self, ws):
        ws.send(self.message)
        logger.info("[PrismMessageHandler] on_open")

    # 获取prismMessage消息
    def get(self):
        return PrismMessage()

    # 组装发布消息
    def publish(self, routing_key, message):
        logger.info("[PrismNotify] publish")
        self.message = self.get().assemble_publish_data(routing_key, message)
        self.socket.on_open = self.on_open
        self.socket.run_forever()

    # 消费信息
    def consume(self):
        logger.info("[PrismNotify] consume")
        self.message = self.get().assemble_consume_date()
        self.socket.on_open = self.on_open
        self.socket.run_forever()

