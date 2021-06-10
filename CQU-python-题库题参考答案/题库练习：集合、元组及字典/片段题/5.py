<<<<<<< HEAD
def classify(x,ls):
=======
def classify(x,ls):
>>>>>>> 91c5edef37c527a60ab0cadc28e08bc788a52119
	    dic['k1'], dic['k2'] = [], []
	    for i in ls:
	        if i > x:
	            dic['k1'].append(i)
	        else:
	            dic['k2'].append(i)
<<<<<<< HEAD

	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

=======

	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

>>>>>>> 91c5edef37c527a60ab0cadc28e08bc788a52119
print(sorted(list(dic.items())))

