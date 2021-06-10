def GCD(m,n): 
    if n==0:      #递归结束条件
          return m

    else:
          return GCD(n, m % n)


a,b=eval(input())
d=GCD(a,b)  #调用自定义函数
print(d)

