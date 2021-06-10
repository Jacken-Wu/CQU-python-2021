nums = eval(input())
new = list(set(nums))

for i in new:
    n = 0
    for j in nums:
        if i == j:
            n += 1
    for k in range(n - 1):
        nums.remove(i)

print(nums)


