l1 = eval(input())
# 拷贝列表
l2 = l1[:]




l1.sort()
l2.sort(reverse=True)
l3 = l1 + l2
# 把偶数位置的元素设置为0
for i in range(len(l3)):
	if i % 2 == 0:
		l3[i] = 0




print(l3)


