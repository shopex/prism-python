# __author__ = 'daixinyu'
# coding=utf8


class PrismMessage:
    def __init__(self):
        self.tag_id = 1

    def assemble_publish_data(self, routing_key, message):
        return "0x01"

    def assemble_ack_date(self):
        return "0x02"

    def assemble_consume_date(self):
        return "0x03"

