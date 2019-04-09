#
import random
# print(random.random())
# print(random.randint(1,8))#包括8

# print(random.choice("hello world"))

# print(random.shuffle([3,2,3,4],random=True))
# print(random.sample([34,5454243,3232,4345],2))
# print(random.randrange(1,10))

def v_code():
    code = ""
    for i in range(5):
        add = random.choice([random.randrange(10),chr(random.randrange(65,90))])
        # if i == random.randint(0,5):
        #     add = random.randrange(10)
        #     code += str(add)
        # else:
        #     add_al = random.randrange(65, 90)
        code += str(add)
    print(code)
v_code()
# print(chr(90))



