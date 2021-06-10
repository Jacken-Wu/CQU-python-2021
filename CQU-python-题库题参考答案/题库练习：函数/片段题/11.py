def add_id(data2):
    for i in range(len(data2)):
        data2[i] = '20' + data2[i]
    return data2


data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

