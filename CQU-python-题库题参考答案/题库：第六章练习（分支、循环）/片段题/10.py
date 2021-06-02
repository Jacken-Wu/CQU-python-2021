def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s = 0
    s_2 = 0
    for i in range(a):
        s += a * 10**(len(str(a)) * i)
        s_2 += s
    print(s_2)

main()

