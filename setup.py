# __author__ = 'daixinyu'
# coding=utf8
from setuptools import setup

VERSION = "0.1"

setup(
    name="prism-python",
    version=VERSION,
    description="ShopEx prismSDK for python",
    author="ShopEx",
    author_email="daixinyu@shopex.cn",
    license="LGPL",
    url="https://github.com/shopex/prism-python",
    packages=["com", "com.shopex","com.shopex.utils", "com.shopex.prism"],
    platforms=["any"],
)