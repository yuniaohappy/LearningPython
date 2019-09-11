getstr = ''

while("bye" != getstr):
    getstr = input("请输入字符，并按Enter键结束：")
    if "hello" == getstr.strip():
        print("start!!!")
    elif "go away" == getstr.strip() or "bye" == getstr.strip():
        print("Goodbye!!!")
        break
    elif "pardon" == getstr.strip():
        getstr = ''
        continue