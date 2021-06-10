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



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

