<<<<<<< HEAD
def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
=======
def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
>>>>>>> 91c5edef37c527a60ab0cadc28e08bc788a52119
def calculate_capital(n, m):
    for year in range(m):
        n *= 1.003
    print('%.4f' % n)
<<<<<<< HEAD

main()

=======

main()

>>>>>>> 91c5edef37c527a60ab0cadc28e08bc788a52119


