<<<<<<< HEAD
def main():
    num = eval(input())
    calculate_e(num)
=======
def main():
    num = eval(input())
    calculate_e(num)
>>>>>>> 91c5edef37c527a60ab0cadc28e08bc788a52119
def calculate_e(n):
    e = 1
    b = 1
    for i in range(1, n+1):
        b *= i
        e += 1 / b
    print('%.6f' % e)
<<<<<<< HEAD

main()
=======

main()
>>>>>>> 91c5edef37c527a60ab0cadc28e08bc788a52119


