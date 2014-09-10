ShopEx Prism sdk (python version)
===============================================

用途
-----------------------------------------------

实现ShopEx Prism 的Python版SDK供第三方使用


功能
-----------------------------------------------

    提供http API调用（GET/POST方式）
    连接WebSocket，可以发布/消费/应答消息
    提供oauth认证

要求
-----------------------------------------------

python sdk 2.6或者以上更高的版本


打包与安装
-----------------------------------------------


1、打包

    git clone https://github.com/shopex/prism-python

    cd prism-python/

    python setup.py sdist  #构建Prism SDK完成，构建SDK位于.dist目录中

2、安装

    tar -zxvf prism-python-0.1.tar.gz

    cd prism-python-0.1

    python setup.py install  #安装Prism SDK完成

使用方法
-----------------------------------------------


###1、提供HTTP API调用(GET/POST)(参考如下TestCase代码)

ps:
```
import unittest

from com.shopex.prism.PrismClient import PrismClient


class PrismClientTestCase(unittest.TestCase):
    def setUp(self):
        self.url = "http://dilbmtcv.apihub.cn/api";
        self.key = "buwb2lii"
        self.secret = "ucr72ygfutspqeuu6s36"
        self.prismClient = PrismClient(self.url, self.key, self.secret)

    def testDoGet(self):
        params = {}
        print self.prismClient.do_get("/platform/notify/status", params)

    def testDoPost(self):
        params = {"data": "hello"}
        print self.prismClient.do_post("/platform/notify/write", params)


if __name__ == '__main__':
    unittest.main()
```

返回是一串json格式的response消息体

###2、OAuth认证

```
url = "http://dilbmtcv.apihub.cn/api"
key = "buwb2lii"
secret = "ucr72ygfutspqeuu6s36"

prism_oauth = PrismOauth(self.url, self.key, self.secret, session)
prism_oauth.require_oauth()   //启动OAuth认证
```

###3、WebSocket

a、建立websocket连接

```
method = "/platform/notify"
prismClient.notify(method);
```

b、发布消息

prismClient.publish("order.new","hello world");

c、开启队列消费

```
prismClient.consume();
prismClient.ack(1);
```







