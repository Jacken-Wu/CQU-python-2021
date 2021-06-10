n = eval(input())
nums = [[str(y)+"*"+str(x)+"="+str(x * y) for x in range(1, y+1)]
        for y in range(1 + n)
]



# print(nums)
for x in nums:
    str1 = " ".join(x)
    print(str1)


