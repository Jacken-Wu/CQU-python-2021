def leapyear(x):
   if x % 400 == 0:
       return True
   elif x % 4 == 0 and x % 100 != 0:
       return True
   return False

year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

