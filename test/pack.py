# __author__ = 'daixinyu'
# coding=utf8
import struct

routing_key = "order.new"
message = "mytest00001"
content_type = "text/plain"


routing_key_pack = struct.pack(">H%ds" % len(routing_key), 2, routing_key)
message_pack = struct.pack(">I%ds" % len(message), 4, message)
content_type_pack = struct.pack(">H%ds" % len(content_type), 2, content_type)

content_pack = struct.pack("%ds%ds%ds" % (len(routing_key_pack), len(message_pack), len(content_type_pack)), routing_key_pack, message_pack, content_type_pack)
print struct.pack("B%ds" % (len(content_pack)), 0x01, content_pack)


