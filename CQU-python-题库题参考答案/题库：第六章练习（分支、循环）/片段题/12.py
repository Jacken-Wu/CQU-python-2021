<<<<<<< HEAD
n=input()
r=1
for i in range(len(n)):

    if(n[i]!=n[-(i+1)]):
        r=0
        break

if r==0:
    print("False")
else:
=======
n=input()
r=1
for i in range(len(n)):

    if(n[i]!=n[-(i+1)]):
        r=0
        break

if r==0:
    print("False")
else:
>>>>>>> 91c5edef37c527a60ab0cadc28e08bc788a52119
    print("True")

