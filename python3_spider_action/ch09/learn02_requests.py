# coding: utf-8

import requests

'''
proxy = '127.0.0.1:9743'
# 如果需要认证
#proxy = 'username:password@127.0.0.1:9743'
proxies = {
    'http': 'http://' + proxy,
    'https': 'https://' + proxy
}
try:
    response = requests.get('http://httpbin.org/get', proxies=proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)
'''

'''
# sockets pip3 install "requests[socks]"
proxy = '127.0.0.1:9743'
proxies = {
    'http': 'socks5://' + proxy,
    'https': 'socks5://' + proxy
}
try:
    response = requests.get('http://httpbin.org/get', proxies=proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)
'''

# socks5 全局设置方式
import requests
import socks, socket

socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', 9742)
socket.socket = socks.socksocket
try:
    response = requests.get('http://httpbin.org/get')
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)