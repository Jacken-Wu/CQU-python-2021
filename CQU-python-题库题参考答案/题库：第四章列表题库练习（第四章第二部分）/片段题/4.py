def Fibonacci(num, n):
    while len(num) < n:
        num.append(num[-2] + num[-1])
    return num[-1]
<<<<<<< HEAD





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))
=======





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))
>>>>>>> 91c5edef37c527a60ab0cadc28e08bc788a52119


