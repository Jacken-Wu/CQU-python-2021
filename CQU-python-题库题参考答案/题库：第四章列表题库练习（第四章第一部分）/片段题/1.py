nums = eval(input())
n = eval(input())
for x in nums:
    if n - x in nums:

        print(True)
        break
else:
    print(False)

