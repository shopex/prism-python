# __author__ = 'daixinyu'
# coding=utf8
from com.shopex import websocket

from com.shopex.prism.PrismMessage import PrismMessage
from com.shopex.utils.LogUtil import logger

# websocket.enableTrace(True)


class PrismNotify:
    # socket
    def __init__(self, ws_url):
        self.socket = websocket.WebSocketApp(ws_url,
                                             on_message=self.on_message,
                                             on_error=self.on_error,
                                             on_close=self.on_close)
        self.socket.on_open = self.on_open
        self.socket.run_forever()

    # 获取prismMessage消息
    def get(self):
        return PrismMessage(self.socket)

    # 组装发布消息
    def publish(self, routing_key, message):
        logger.info("[PrismNotify] publish")
        self.socket.send(self.get().assemble_publish_data(routing_key, message))

    # 消费信息
    def consume(self):
        logger.info("[PrismNotify] consume")
        self.socket.send(self.get().assemble_consume_date())

    # # ack消息应答
    # def ack(self):
    # self.socket.send(self.get().assemble_ack_date())

    def on_message(self, socket, frame):
        logger.info("[PrismNotify] socket on_message")

    def on_open(self, socket):
        logger.info("[PrismNotify] socket on_open")

    def on_error(self, socket, error):
        logger.info("[PrismNotify] socket on_error,error info is %s \t \n" % (error))

    def on_close(self, socket):
        logger.info("[PrismNotify] socket on_close")