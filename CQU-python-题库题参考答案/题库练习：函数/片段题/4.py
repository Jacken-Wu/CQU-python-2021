def job(time):  
#time存放三个人完成三个任务的时间。time的结构是二维列表。
#可以用穷举求解。可以用set判断某种调度方案是否有重复人员，例如“AAB”
#函数有两个返回值，一个是最优方案的时间，一个是执行顺序(字符串)
    m = 999
    menber = ['A', 'B', 'C']
    l = []
    for x in range(3):
        men_list = []
        men_list.append(menber[x])
        for y in range(3):
            men_list_2 = men_list[:]
            men_list_2.append(menber[y])
            for z in range(3):
                men_list_3 = men_list_2[:]
                men_list_3.append(menber[z])
                if len(set(men_list_3)) == 3:
                    m_2 = sum([time[0][x], time[1][y], time[2][z]])
                    if m_2 < m:
                        m = m_2
                        l = men_list_3
    s = ''.join(l)
    return [m, s]


time_all=[]
for x in range(3):#读3行        
      time_one=input().split()
      time_one=[eval(x) for x in time_one]
      time_all.append(time_one)
result=job(time_all)
for x in result:
    print(x,end=" ")

