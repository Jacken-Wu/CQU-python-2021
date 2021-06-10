def calDegrees(n):
	max_n = 0
	n_2 = list(set(n))
	for i in n_2:
		m = 0
		while i in n:
			n.remove(i)
			m += 1
		if m > max_n:
			max_n = m
	return max_n 
<<<<<<< HEAD



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
=======



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
>>>>>>> 91c5edef37c527a60ab0cadc28e08bc788a52119
print(d)

