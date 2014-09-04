# coding=utf8

import websocket


def on_message(ws, message):
    print "[on_message] %s \t \n" % (message)


def on_error(ws, error):
    ws.send("error")
    print "[on_error] %s \t \n" % (error)


def on_close(ws):
    ws.send("closed")
    print "### closed ###"


def on_open(ws):
    ws.send("11")
    print "[on_open]"


if __name__ == "__main__":
    # websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://localhost:3398/",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()

