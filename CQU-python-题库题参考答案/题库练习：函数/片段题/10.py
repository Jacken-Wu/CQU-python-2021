def isPrime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def reverseNumber(num):
    num_reverse = 0
    while num != 0:
        num_reverse *= 10
        num_reverse += num % 10
        num //= 10
    return num_reverse


N = int(input())
for n in range(1,N+1):
    if isPrime(n) and reverseNumber(n) == n:
        print(n) 

