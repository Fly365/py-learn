# -*- coding: utf-8 -*-
import json

strList = '[1,2,3,4,5]'
# Expecting property name enclosed in double quotes 要用双引号
strDict = '{"city":"北京", "name":"fly"}'

json.loads(strList)

json.loads(strDict)

# 编码识别模块
import chardet

listStr = [1,2,3,4]
tupleStr = (1,2,3,4)
dictStr = {"city":"上海","name":"fly"}

json.dumps(listStr)
json.dumps(tupleStr)

# 注意：json.dumps() 序列化时默认使用的ascii编码
# 添加参数 ensure_ascii=False 禁用ascii编码，按utf-8编码
# chardet.detect()返回字典, 其中confidence是检测精确度
json.dumps(dictStr)

chardet.detect(json.dumps(dictStr))

chardet.detect(json.dumps(dictStr,ensure_ascii=False))