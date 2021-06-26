a = input()
b = input()
la = len(a)
lb = len(b)
#建立二维列表，行数la+1，列数lb+1,初值为0
res = [[0 for x in range(lb + 1)] for y in range(la + 1)]

lc = []
mmax = 0
for i in range(1, la+1):
   for j in range(1, lb+1):
      if a[i-1] == b[j-1]:
         res[i][j] = res[i-1][j-1] + 1
         if(res[i][j] > mmax
):
            mmax = res[i][j]
            
print(mmax)


