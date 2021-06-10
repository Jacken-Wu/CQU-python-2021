def matrix(n=2): 
    l = [['*' for x in range(n)] for y in range(n)]
    s = ''
    for i in l:
        s += ' '.join(i) + '\n'
    print(s)


number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(int(number))
  #有实参调用自定义函数

