def caculate(*t):
    a = 1
    for x in t:
        a *= x
    return a


s = input().split()
t = [float(x) for x in s]
print("%.4f" % caculate(*t))   

