def  myFun(a,b):
       a = list(map(int, list(str(a))))
       b = list(map(int, list(str(b))))
       while len(a) < len(b):
           a.insert(0, 0)
       while len(b) < len(a):
           b.insert(0, 0)
       n = 0
       for i in range(len(a)):
           n += a[i]*b[i]
       return n


num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

