import requests

response = requests.get("https://www.12306.cn/mormhweb/")

print(response.text)