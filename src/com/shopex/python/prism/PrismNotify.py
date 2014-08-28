# __author__ = 'daixinyu'
# coding=utf8
from com.shopex.python.config import config
from com.shopex.python.prism.PrismMessage import PrismMessage


class PrismNotify:
    # socket
    def __init__(self):
        self.method = config.notify_method
        self.socket = None

    # 获取prismMessage消息
    def get(self):
        return PrismMessage(self.socket)

    # 组装发布消息
    def publish(self, routing_key, message, content_type):
        self.socket.send(self.get().assemble_publish_data())

    # 消费信息
    def consume(self):
        self.socket.send(self.get().assemble_consume_date())

    # ack消息应答
    def ack(self):
        self.socket.send(self.get().assemble_ack_date())