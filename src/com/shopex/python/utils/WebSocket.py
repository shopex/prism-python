# __author__ = 'daixinyu'
# coding=utf8
import threading
import base64
import hashlib
import struct
import socket
import sys
from com.shopex.python.utils.LogUtil import logger


class WebSocket(threading.Thread):
    def __init__(self, connection, address):
        threading.Thread.__init__(self)
        self.connection = connection
        self.address = address

    def run(self):
        logger.debug('WebSocket Start...')
        if self.handshake():
            while True:
                receive_buff = self.receive_message()
                self.send_date(receive_buff)

    def send_date(self, pData):
        if (pData == False):
            return False
        else:
            pData = str(pData)
        token = "\x81"
        length = len(pData)
        if length < 126:
            token += struct.pack("B", length)
        elif length <= 0xFFFF:
            token += struct.pack("!BH", 126, length)
        else:
            token += struct.pack("!BQ", 127, length)
        pData = '%s%s' % (token, pData)
        self.connection.send(pData)
        return True

    # 接收客户端发送过来的消息,并且解包
    def receive_message(self):
        try:
            pData = self.connection.recv(2048)
            if not len(pData):
                return False
        except Exception, e:
            return False
        else:
            code_length = ord(pData[1]) & 127
            if code_length == 126:
                masks = pData[4:8]
                data = pData[8:]
            elif code_length == 127:
                masks = pData[10:14]
                data = pData[14:]
            else:
                masks = pData[2:6]
                data = pData[6:]
            raw_str = ""
            i = 0
            for d in data:
                raw_str += chr(ord(d) ^ ord(masks[i % 4]))
                i += 1
            return raw_str

    # 握手
    def handshake(self):
        headers = {}
        shake = self.connection.recv(1024)
        if not len(shake):
            return False
        header, data = shake.split('\r\n\r\n', 1)
        for line in header.split("\r\n")[1:]:
            key, value = line.split(": ", 1)
            headers[key] = value
        if (headers.has_key("Sec-WebSocket-Key") == False):
            logger.debug("This socket is not Websocket,so close it!")
            self.connection.close()
            return False
        szOrigin = headers["Origin"]
        szKey = base64.b64encode(
            hashlib.sha1(headers["Sec-WebSocket-Key"] + '258EAFA5-E914-47DA-95CA-C5AB0DC85B11').digest())
        szHost = headers["Host"]
        our_handshake = "HTTP/1.1 101 Switching Protocols\r\n" \
                        "Upgrade:websocket\r\n" \
                        "Connection: Upgrade\r\n" \
                        "Sec-WebSocket-Accept:" + szKey + "\r\n" \
                                                          "WebSocket-Origin:" + szOrigin + "\r\n" \
                                                                                           "WebSocket-Location: ws://" + szHost + "/WebManagerSocket\r\n" \
                                                                                                                                  "WebSocket-Protocol:WebManagerSocket\r\n\r\n"

        self.connection.send(our_handshake)
        return True


class WebSocketInit:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def init_socket(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.bind((self.host, self.port))  # 绑定本地地址,端口self.port
            sock.listen(100)
        except Exception, e:
            logger.debug("[WebSocketInit] %s \t \n" % (e))
            sys.exit()
        while True:  # 创建一个死循环,接受客户端
            connection, address = sock.accept()
            web_socket = WebSocket(connection, address)
            web_socket.start()


if __name__ == "__main__":
    from com.shopex.python.config import config

    WebSocketInit(config.host, config.port).init_socket()




