scores = [ ('Emma ', 89 , 90 , 59),
           ('Edith', 99 , 49 , 59),
           ('Sophia', 99 , 60, 20),
           ('May', 40 , 94 , 59),
           ('Ashley', 89 , 90 , 59),
           ('Arny', 89 , 90, 69),
           ('Lucy', 79 , 90 , 59 ),
           ('Gloria', 85 , 90 , 59),
           ('Abby', 89 , 91 , 90)]

def handel_filter(score):
    """这个是handel_filter函数"""
    s = sorted(score[1:])
    if s[-2] > 80 and s[0] < 60:
        return True
    if s[-1] > 90 and s[1] < 60:
        return True
    if s[-2] > 80 and sum(s) / len(s) < 60:
        return True
    return False
aa = list(filter(handel_filter,scores))
print(aa)
print(handel_filter.__doc__)

