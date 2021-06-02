def work(a) :
    ans = dict()
    for n in range(a + 1):
        ans[n] = 1
        for i in range(1, n + 1):
            ans[n] *= i
    return ans

	

a = int(input())
ans = work(a)
print(ans)

