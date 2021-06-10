def  fibo(n):
       if n<=2:
             return 1
       else:
              return fibo(n-1) + fibo(n-2)
  

n=int(input())
if n<=0 or n>20:
       print("rangeout")
else:
       print(fibo(n))
  #调用自定义函数

