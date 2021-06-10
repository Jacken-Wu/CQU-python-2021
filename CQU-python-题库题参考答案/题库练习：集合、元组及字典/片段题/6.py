def findMax(lst):
    max_num = 0
    lst_num = 0
    for i in range(len(lst)):
        if lst[i] > max_num:
            max_num = lst[i]
            lst_num = i
    return {lst_num: max_num}
<<<<<<< HEAD

ls=eval(input())
result=findMax(ls)
for  i,j  in  result.items():
          print(str(i)+":"+str(j))
=======

ls=eval(input())
result=findMax(ls)
for  i,j  in  result.items():
          print(str(i)+":"+str(j))
>>>>>>> 91c5edef37c527a60ab0cadc28e08bc788a52119


