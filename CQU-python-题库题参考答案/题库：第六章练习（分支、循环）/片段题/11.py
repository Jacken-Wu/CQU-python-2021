<<<<<<< HEAD
def leapyear(x):
=======
def leapyear(x):
>>>>>>> 91c5edef37c527a60ab0cadc28e08bc788a52119
   if x % 400 == 0:
       return True
   elif x % 4 == 0 and x % 100 != 0:
       return True
   return False
<<<<<<< HEAD

year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
=======

year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
>>>>>>> 91c5edef37c527a60ab0cadc28e08bc788a52119
    print("In %d February has 28 days."%year)

