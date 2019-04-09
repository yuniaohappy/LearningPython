from urllib.request import urlopen
from bs4 import BeautifulSoup
while True:
    key = input("请输入要翻译的内容：")
    if key == 'q':
        break
    url = "https://cn.bing.com/dict/search?q=" + key
    response = urlopen(url)
    soup = BeautifulSoup(response,"html.parser")
    li = soup.select("div.qdef li")

    for item in li:
        print(item.text)