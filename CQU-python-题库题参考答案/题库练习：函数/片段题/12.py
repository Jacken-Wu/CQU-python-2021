def  stuid(data2):
    for i in range(len(data2)):
        data2[i] = data2[i][: 8]
    return data2


data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

