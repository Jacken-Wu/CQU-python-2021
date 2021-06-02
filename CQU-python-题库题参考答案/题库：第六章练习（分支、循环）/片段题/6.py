salary = float(input())
tax = 0.0
salary -= 5000*12
if salary <= 0:
    tax = 0.0
elif salary <= 36000:
    tax = salary * 0.03
elif salary <= 144000:
    tax = salary * 0.1 - 2520
elif salary <= 300000:
   tax  =  salary  *  0.2  -  16920

elif salary <= 420000:
    tax = salary * 0.25 - 31920
elif salary <= 660000:
    tax = salary * 0.3 - 52920
elif salary <= 960000:
    tax = salary * 0.35 - 85920
else:
    tax = salary * 0.45 - 181920
salary  +=  5000*12
salary -= tax

print("%.2f"%tax)
print("%.2f"%salary)

