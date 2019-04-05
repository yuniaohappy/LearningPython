class Page:
    def __init__(self,page):
        try:
            self.page = int(page)
        except:
            self.page = 1
    @property
    def start(self):
        p = (self.page -1) * 10
        return p
    @property
    def end(self):
        p = self.page * 10
        return p
s = input("请输入输入数字：")
page = Page(s)
lis = []
for i in range(1000):
    lis.append(i)

print(lis[page.start:page.end])