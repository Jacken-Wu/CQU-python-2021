def f1(nums):
    n = []
    for i in nums:
        if i % 2 == 1:
            n.append(i)
    for i in nums:
        if i % 2 == 0:
            n.append(i)
          
    return n
    
<<<<<<< HEAD


nums = eval(input())

=======


nums = eval(input())

>>>>>>> 91c5edef37c527a60ab0cadc28e08bc788a52119
print(f1(nums))  # 调用自定义函数

