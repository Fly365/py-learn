# ecoding=utf-8

# urlparse
from urllib.parse import urlparse

result = urlparse("http://wwww.baidu.com/index.html;user?id=5#comment")
print(type(result), result)

# urlunparse 是相应的urlunparse对立方法
from urllib.parse import urlunparse
data = ["http", "www.baidu.com", "index.html", "user", "a=6", "comment"]
print(urlunparse(data))

# urlsplit()
from urllib.parse import urlsplit
result = urlsplit("http://www.baidu.com/index.html;user?id=5#comment")
print(result)

# urlunsplit()
from urllib.parse import urlunsplit
data = ["http","www.baidu.com","index.html","a=6","comment"]
print(urlunsplit(data))

# urljoin
from urllib.parse import urljoin
print(urljoin("http://www.baidu.com", "?category=2#comment"))

# urlencode,在构造 GET 请求参数时候非常有用
from urllib.parse import urlencode
params = {
    "name": "jerry",
    "age": 20
}
base_url = "http://www.baidu.com?"
url = base_url + urlencode(params)
print(url)

# parse_qs()，对于 GET 反序列化，将参数 转回 字典
from urllib.parse import parse_qs
query = "name=jerry&age=20"
print(parse_qs(query))

# parse_qsl() 将参数转为 元组
# 列表中每一个元素都是一个元组，元组的第一个内容是参数名，第二个是参数值
from urllib.parse import parse_qsl
query = "name=jerry&age=20"
print(parse_qsl(query))

# quote()，将内容转化为URL编码格式，URL中带有中文参数时
from urllib.parse import quote
keyword = "中文"
url = "http://www.baidu.com/s?wd=" + quote(keyword)
print(url)

# unquote()，进行URL解码
from urllib.parse import unquote
url = "http://www.baidu.com/s?wd=%E4%B8%AD%E6%96%87"
print(unquote(url))