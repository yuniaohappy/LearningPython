#重试功能
def retry(attr):
    def decorator(fun):
        def wrapper(*args,**kwargs):
            att = 0
            while att < attr:
                print(att)
                try:
                    return fun(*args,**kwargs)
                except Exception as e:
                    att += 1
        return wrapper
    return decorator

import requests
@retry(attr=3)
def get_response(url):
    r = requests.get(url)
    return r

# URL = 'http://www.163.com'
# r = get_response(URL)
# print(r.content.decode('gbk'))

URL = 'http://www.163234123.com'
r = get_response(URL)
print(r)
with open():
    pass

