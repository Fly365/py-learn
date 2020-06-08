# coding: utf-8
from attr import attrs, attr

@attrs
class Proxy(object):
    host = attr(type=str, default=None)
    port = attr(type=int, default=None)