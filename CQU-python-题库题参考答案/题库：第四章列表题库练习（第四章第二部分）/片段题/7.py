def maxsum(numl):
	numl.sort()
	return sum(numl[::2])





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

