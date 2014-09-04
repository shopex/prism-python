# __author__ = 'daixinyu'
# coding=utf8


class PrismMessage:
    def __init__(self, socket):
        self.socket = socket
        self.tag_id = 1

    def assemble_publish_data(self, routing_key, message):
        return "1"

    def assemble_ack_date(self):
        return "2"

    def assemble_consume_date(self):
        return "3"

