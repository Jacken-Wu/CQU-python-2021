<<<<<<< HEAD
encoding='UTF-8'
n=eval(input())
k=2
while k <= n-1:
    r = n % k
    if r == 0:
        break

    else:
        k=k+1
if r != 0:

    print(n,"is a prime number")
else:
=======
encoding='UTF-8'
n=eval(input())
k=2
while k <= n-1:
    r = n % k
    if r == 0:
        break

    else:
        k=k+1
if r != 0:

    print(n,"is a prime number")
else:
>>>>>>> 91c5edef37c527a60ab0cadc28e08bc788a52119
    print(n,"is not a prime number")

