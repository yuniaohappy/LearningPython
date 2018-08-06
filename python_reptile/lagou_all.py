from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import time
import pymysql

con = pymysql.connect(host="127.0.0.1", user="root", password="",
                      database="test", charset="utf8")
cursor = con.cursor()

'''返回首页所有的链接'''


def getAllLinks():
    response = urlopen("https://www.lagou.com/")
    soup = BeautifulSoup(response, "html.parser")
    '''主类的链接'''
    main = soup.select("div.menu_sub a")
    main = [item.get("href") for item in main]
    sub = soup.select("div.menu_main > a")
    sub = [item.get("href") for item in sub]
    '''将列表list对象转换成set对象'''
    main = set(main)
    sub = set(sub)
    print(len(main))
    print(len(sub))
    '''合并两个set，去掉重复的元素'''
    allLink = main.union(sub)
    return list(allLink)


'''对于每一个分类链接，抓取数据，保存到MySQL数据库中'''


def crawl(link):
    for page in range(1, 31):
        print("准备爬取第%d页数据" % page)
        url = link + str(page) + "/"
        request = Request(url)
        request.add_header("Cookie",
                           "user_trace_token=20170503123803-01717bd30af1485ab77a20f46b8241ce; LGUID=20170503123804-4be39095-2fba-11e7-b512-5254005c3644; JSESSIONID=ABAAABAAAGGABCB084DC2C66D4E087863CAE75E388751F1; index_location_city=%E5%8C%97%E4%BA%AC; TG-TRACK-CODE=index_navigation; SEARCH_ID=b66f16664e174eceb3622cd444378eb4; _gid=GA1.2.528461640.1498375158; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1498375158; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1498376465; _ga=GA1.2.650217228.1493786284; LGSID=20170625151913-970e3518-5976-11e7-9e77-5254005c3644; LGRID=20170625154101-a27d4440-5979-11e7-9e77-5254005c3644")
        response = urlopen(request)
        if url != response.geturl():
            print("该页没有数据，返回，准备爬取下一个分类")
            break
        soup = BeautifulSoup(response, "html.parser")
        title = soup.select("a.position_link h2")
        pos = soup.select("a.position_link em")
        money = soup.select("div.p_bot div.li_b_l")
        company = soup.select("div.company_name a")
        tags = soup.select("div.list_item_bot div.li_b_l")
        domain = soup.select("div.industry")
        adv = soup.select("div.li_b_r")

        for i in range(len(title)):
            _title = title[i].text
            _pos = pos[i].text
            temp = list(money[i].stripped_strings)
            _money = temp[0]
            '''将字符串根据参数指定的内容进行切割，返回切割之后的结果（列表）'''
            temp = temp[1].split(" / ")
            _exp = temp[0]
            _edu = temp[1]
            _company = company[i].text
            _tags = ",".join(list(tags[i].stripped_strings))
            temp = domain[i].text.strip().split(" / ")
            if len(temp) == 2:
                _domain = temp[0]
                _phase = temp[1]
            else:
                _domain = "无"
                _phase = "无"
                '''strip也可以去掉两端指定的字符集'''
            _adv = adv[i].text.strip("“”")
            cursor.execute("insert into lagou(title, pos, money, exp, edu," +
                           "company, tags, domain, phase, adv) values(%s,%s,%s,%s," +
                           "%s,%s,%s,%s,%s,%s)",
                           [_title, _pos, _money, _exp, _edu, _company, _tags, _domain,
                            _phase, _adv])
            '''让程序休眠参数指定的时间（秒），时间可以是小数'''
        con.commit()
        time.sleep(1)


'''主函数，程序运行的开始'''


def main():
    links = getAllLinks()
    for link in links:
        crawl(link)


main()
cursor.close()
con.close()
# crawl("https://www.lagou.com/zhaopin/ziranyuyanchuli/")