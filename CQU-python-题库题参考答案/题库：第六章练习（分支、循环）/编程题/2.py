num = int(input())
b = False
if num % 2 == 0 or num % 5 == 0:
    if num % 10:
        b = True
print(b) 

