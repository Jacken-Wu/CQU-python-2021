def f1(nums):
    n = []
    for i in nums:
        if i % 2 == 1:
            n.append(i)
    for i in nums:
        if i % 2 == 0:
            n.append(i)
          
    return n
    


nums = eval(input())

print(f1(nums))  # 调用自定义函数

