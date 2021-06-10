def medium(number2):
    number2.sort()
    x=len(number2)//2
    if x * 2 != len(number2):

        med=number2[x]
    else:
        med=(number2[x]+number2[x-1])/2
    return med


origin=input().split()
number1=[eval(x) for x in origin]
print("%.2f"%medium(number1))

