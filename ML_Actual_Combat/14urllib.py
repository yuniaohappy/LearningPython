from urllib.request import urlopen
url = "https://www.python.org"
response = urlopen(url)
content = response.read()
content = content.decode("utf-8")
print(content)