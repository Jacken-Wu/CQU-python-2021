<<<<<<< HEAD
nums = eval(input())
sum = eval(input())
for x in range(len(nums)):
    n = sum-nums[x]
    if n in nums:
        if n != nums[x]:

            print(True)
            break
        else:
            if n in nums[:x] or n in nums[x+1:]:

                print(True)
                break
else:
=======
nums = eval(input())
sum = eval(input())
for x in range(len(nums)):
    n = sum-nums[x]
    if n in nums:
        if n != nums[x]:

            print(True)
            break
        else:
            if n in nums[:x] or n in nums[x+1:]:

                print(True)
                break
else:
>>>>>>> 91c5edef37c527a60ab0cadc28e08bc788a52119
    print(False)

