def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(n, m):
    for year in range(m):
        n *= 1.003
    print('%.4f' % n)

main()



