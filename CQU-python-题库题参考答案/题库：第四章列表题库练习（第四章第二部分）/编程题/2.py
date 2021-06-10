nums = eval(input())
num = 0
for i in range(len(nums)):
    num_0 = min(nums)
    num += num_0 * (10 ** i)
    nums.remove(num_0)
print(num)


