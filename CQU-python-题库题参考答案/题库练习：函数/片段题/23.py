def prime(n):
    for i in range(2, n):
 #for循环
        for j in range(2,i):
            if(i%j==0):
                 break

        else:
            if sum_digits(i) == 10:
 #调用sum_digits函数计算各位数字之和，判断是否为10
                print(i,end=" ")
            

def sum_digits(m): #计算各位数字之和
    s=str(m)
    mysum=0
    for k in s:
        mysum += int(k)
   #累加求和
    return mysum 

number=eval(input())
prime(number)

