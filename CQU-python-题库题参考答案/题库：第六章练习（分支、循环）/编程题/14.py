string = input()
nums = [0, 0, 0, 0]
for c in string:
    if 65 <= ord(c) <= 90 or 97 <= ord(c) <= 122:
        nums[0] += 1
    elif c == ' ':
        nums[1] += 1
    elif 48 <= ord(c) <= 57:
        nums[2] += 1
    else:
        nums[3] += 1
print(' '.join(map(str, nums)))

