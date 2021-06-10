<<<<<<< HEAD
def work(a) :
=======
def work(a) :
>>>>>>> 91c5edef37c527a60ab0cadc28e08bc788a52119
    ans = dict()
    for n in range(a + 1):
        ans[n] = 1
        for i in range(1, n + 1):
            ans[n] *= i
    return ans
<<<<<<< HEAD

	

a = int(input())
ans = work(a)
=======

	

a = int(input())
ans = work(a)
>>>>>>> 91c5edef37c527a60ab0cadc28e08bc788a52119
print(ans)

