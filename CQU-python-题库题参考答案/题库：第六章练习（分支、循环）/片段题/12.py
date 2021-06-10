n=input()
r=1
for i in range(len(n)):

    if(n[i]!=n[-(i+1)]):
        r=0
        break

if r==0:
    print("False")
else:
    print("True")

