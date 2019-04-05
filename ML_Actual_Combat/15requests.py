import requests

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
url = "http://new.qq.com/ch/tech/"

res = requests.get(url,headers=headers)
print(res.status_code)
print(res.headers)
print(res.text)