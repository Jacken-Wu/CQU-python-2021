def f(x):
    if x < 20:
        return x ** 2 * 6 + 1
    elif x < 40:
        return pow(x * 3 - 60, 0.5)
    return 100 / (x + 1)


print('%.2f' % f(float(input())))

