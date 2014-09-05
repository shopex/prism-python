shopex Prism sdk (python version)

用途

实现shopex Prism 的Python版SDK供第三方使用


功能

    提供http API调用（GET/POST方式）
    连接Websocket，可以发布/消费/应答消息
    提供oauth认证

要求

python sdk 2.6或者以上更高的版本


打包与安装

下载安装prism-pyhton SDK
git clone https://github.com/shopex/prism-python
cd prism-python/
python setup.py sdist  构建Prism SDK完成，构建SDK位于.dist目录中

安装
tar -zxvf prism-python-0.1.tar.gz
cd prism-python-0.1
python setup.py install 安装Prism SDK完成



