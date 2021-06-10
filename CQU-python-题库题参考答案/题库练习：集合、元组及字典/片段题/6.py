def findMax(lst):
    max_num = 0
    lst_num = 0
    for i in range(len(lst)):
        if lst[i] > max_num:
            max_num = lst[i]
            lst_num = i
    return {lst_num: max_num}

ls=eval(input())
result=findMax(ls)
for  i,j  in  result.items():
          print(str(i)+":"+str(j))


