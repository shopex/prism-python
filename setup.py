# __author__ = 'daixinyu'
# coding=utf8
from setuptools import setup, find_packages
from com.version import version


setup(
    name="prism-python",
    version=version,
    description="ShopEx prismSDK for python",
    long_description=open("README.md").read(),
    packages=find_packages(),
    author="ShopEx",
    author_email="daixinyu@shopex.cn",
    license="LGPL",
    url="https://github.com/shopex/prism-python",
    platforms=["README.md"],
)