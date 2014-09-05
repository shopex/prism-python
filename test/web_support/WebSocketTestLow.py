# ! encoding=utf-8
'''
@author: XinYuDai
@date: 14-9-5
'''
from com.shopex.websocket import create_connection
ws = create_connection("ws://localhost:3398/notify/login?id=1")
print "Sending 'Hello, World'..."
ws.send("Hello, World")
print "Sent"
print "Reeiving..."
result =  ws.recv()
print "Received '%s'" % result
ws.close()