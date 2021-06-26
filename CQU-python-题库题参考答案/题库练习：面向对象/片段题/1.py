class Book:
    def __init__(self, name, id, money):
        self.name = name
        self.id = id
        self.money = float(money)

    def __del__(self):
        print('Book destroyed-%s,%s,%.2f' % (self.name, self.id, self.money))



sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

