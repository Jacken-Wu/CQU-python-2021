from math import *

class Root:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def getDiscriminant(self):
        return self.b**2 - 4*self.a*self.c

    def getRoot1(self):
        return (-self.b + sqrt(self.getDiscriminant())) / (2 * self.a)

    def getRoot2(self):
        return (-self.b - sqrt(self.getDiscriminant())) / (2 * self.a)


a=float(input()) 
b=float(input()) 
c=float(input()) 

root=Root(a,b,c)
if root.getDiscriminant()>0:
    print("{:.2f}".format(root.getRoot1()))
    print("{:.2f}".format(root.getRoot2()))
elif root.getDiscriminant()==0:
    print("{:.2f}".format(root.getRoot1()))
else:
    print("No Root!")


