# coding: utf-8
from ..schemas import Proxy
import re

def is_valid_proxy(data):
    return re.match('\d+\.\d+\.\d+\:\d+', data)

def convert_proxy_or_proxies(data):
    """convert list of str to valid proxies or proxy"""
    if not data:
        return None
    # if list of proxies
    if isinstance(data, list):
        result = []
        for item in data:
            # skip invalid item
            item = item.strip()
            if not is_valid_proxy(item): continue
            host, port = item.split(':')
            result.append(Proxy(host=host, port=int(port)))
        return result
    if isinstance(data, str) and is_valid_proxy(data):
        host, port = data.split(':')
        return Proxy(host=host, port=int(port))