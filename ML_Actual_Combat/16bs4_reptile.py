# import requests
# from bs4 import BeautifulSoup
#
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
# url = "https://new.qq.com"
#
# Soup = BeautifulSoup(requests.get(url=url,headers=headers).text.encode("utf-8"),"lxml")
# em = Soup.find_all()
# print(em)
# for i in em:
#     title = i.meta.get_text()
#     # link = i.a['href']
#     print({'标题':title,'链接':link})

import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}
url = 'http://news.qq.com/'

html = requests.get(url = url, headers = headers)
con = etree.HTML(html.text)

title = con.xpath('//em[@class="f14 l24"]/a/text()')
link = con.xpath('//em[@class="f14 l24"]/a/@href')
for i in zip(title, link):
    print({'标题': i[0],
           '链接': i[1]
    })