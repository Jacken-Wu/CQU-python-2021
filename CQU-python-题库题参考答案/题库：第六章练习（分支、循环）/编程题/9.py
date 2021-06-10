<<<<<<< HEAD
stu = int(input())
stu_list=[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],
['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],
['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],
['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],
['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
f = True
num = 1
while num != 0:
    num = len(stu_list) // 2
    if stu > int(stu_list[num][0]):
        stu_list = stu_list[num+1:]
    elif stu < int(stu_list[num][0]):
        stu_list = stu_list[:num]
    elif stu == int(stu_list[num][0]):
        print(''.join(stu_list[num]))
        f = False
        break

if f:
    print(None)
=======
stu = int(input())
stu_list=[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],
['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],
['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],
['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],
['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
f = True
num = 1
while num != 0:
    num = len(stu_list) // 2
    if stu > int(stu_list[num][0]):
        stu_list = stu_list[num+1:]
    elif stu < int(stu_list[num][0]):
        stu_list = stu_list[:num]
    elif stu == int(stu_list[num][0]):
        print(''.join(stu_list[num]))
        f = False
        break

if f:
    print(None)
>>>>>>> 91c5edef37c527a60ab0cadc28e08bc788a52119

