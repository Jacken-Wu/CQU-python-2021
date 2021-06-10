<<<<<<< HEAD
luo_nums = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
    'A': 0
}
luo = input()
length = len(luo)
luo += 'A'

num = 0
for i in range(length):
    if luo_nums[luo[i]] < luo_nums[luo[i+1]]:
        num -= luo_nums[luo[i]]
    else:
        num += luo_nums[luo[i]]

print(num)
=======
luo_nums = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
    'A': 0
}
luo = input()
length = len(luo)
luo += 'A'

num = 0
for i in range(length):
    if luo_nums[luo[i]] < luo_nums[luo[i+1]]:
        num -= luo_nums[luo[i]]
    else:
        num += luo_nums[luo[i]]

print(num)
>>>>>>> 91c5edef37c527a60ab0cadc28e08bc788a52119

