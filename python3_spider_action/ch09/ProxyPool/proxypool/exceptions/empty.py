# coding: utf-8
class PoolEmptyException(Exception):
    def __str__(self):
        """proxypool is used out"""
        return repr('no proxy in proxypool')