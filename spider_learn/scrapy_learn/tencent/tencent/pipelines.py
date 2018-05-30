# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class TencentPipeline(object):
    def __init__(self):
        # 打开方式改成w,不要用wb。b代表二进制
        # a bytes-like object is required, not 'str'
        self.file = open("tencent.json","w")

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(content)
        return item

    def close_spider(self,spider):
        self.file.close()


class myEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,bytes):
            return str(obj,encoding="utf-8")
        return json.JSONEncoder.default(self,obj)
