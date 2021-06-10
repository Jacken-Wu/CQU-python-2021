<<<<<<< HEAD
nums1 = eval(input())  # 输入列表
nums2 = eval(input())
nums1.sort()  # 排序
nums2.sort()
arr = []
i = j = 0
while i < len(nums1) and j < len(nums2):  # 相互比较开始
    if nums1[i] < nums2[j]:
        i += 1
    elif nums1[i] > nums2[j]:
        j += 1

    else:
        arr.append(nums1[i])

        i += 1
        j += 1
for x in arr:
    while arr.count(x) > 1:
        arr.remove(x)



print(arr)  # 输出
=======
nums1 = eval(input())  # 输入列表
nums2 = eval(input())
nums1.sort()  # 排序
nums2.sort()
arr = []
i = j = 0
while i < len(nums1) and j < len(nums2):  # 相互比较开始
    if nums1[i] < nums2[j]:
        i += 1
    elif nums1[i] > nums2[j]:
        j += 1

    else:
        arr.append(nums1[i])

        i += 1
        j += 1
for x in arr:
    while arr.count(x) > 1:
        arr.remove(x)



print(arr)  # 输出
>>>>>>> 91c5edef37c527a60ab0cadc28e08bc788a52119


