def compute_variance(number2):
    ave=sum(number2)/len(number2)
    mySum=0
    for x in number2:

        mySum+=(x-ave)**2
    variance=mySum/len(number2)
    return variance


origin=input().split()
number1=[eval(x) for x in origin]
print("%.2f"%compute_variance(number1))

