#输入
a = input()
b = input('你算什么：')
c = input()
a = int(a)
c = int(c)

#运算
if b =='加':
    print('结果为：',a+c)
elif b=='减':
    if a >= c:
        print('结果为：',a-c)
    elif a <= c:
        print('结果为：',c-a)
elif b=='乘':
    print('结果为：',a*c)
elif b=='除':
    if a >= c:
        print('结果为：',a/c)
    elif a<= c:
        print('结果为：',c/a)