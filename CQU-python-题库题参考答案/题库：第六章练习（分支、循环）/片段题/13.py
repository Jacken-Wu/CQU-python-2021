def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(n):
    e = 1
    b = 1
    for i in range(1, n+1):
        b *= i
        e += 1 / b
    print('%.6f' % e)

main()


