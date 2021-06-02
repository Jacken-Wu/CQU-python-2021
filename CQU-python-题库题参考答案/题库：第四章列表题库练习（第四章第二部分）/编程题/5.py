def whether(n, nums_1):
    if n in nums_1:
        nums_1.remove(n)
        if n in nums_1:
            return False
        else:
            return True
    return False


nums = eval(input())
nums_2 = []
for i in range(max(nums) + 1):
    if whether(i, nums):
        nums_2.append(i)

if len(nums_2):
    string = str(nums_2).replace(' ', '').replace('[', '').replace(']', '')
    print(string)
else:
    print('False')


