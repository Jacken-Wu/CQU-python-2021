#class Stock
class Stock:
    """Stock Information Class"""

    def __init__(self, code, name, yes, to):
        self.__code = code
        self.__name = name
        self.__yes = yes
        self.__to = to

    def getCode(self):
        return self.__code

    def getName(self):
        return self.__name

    def getPriceYesterday(self):
        return self.__yes

    def setPriceYesterday(self, yes):
        self.__yes = yes

    def getPriceToday(self):
        return self.__to

    def setPriceToday(self, to):
        self.__to = to

    def getChangePercent(self):
        return (self.__to - self.__yes) / self.__yes



sCode = input() #Stock Code
sName = input() #Stock Name
priceYesterday = float(input())  #Price/Yesterday
priceToday = float(input())  #Price Today
s = Stock(sCode,sName,priceYesterday,priceToday)
print("Code:",s.getCode())
print("Name:",s.getName())
print("Price/Yesterday:%.2f\nPrice Today:%.2f" % (s.getPriceYesterday(),s.getPriceToday()))
s.setPriceYesterday(50.25)
print("Edit Price/Yesterday To:%.2f" % 50.25)
print("Price Change Percentage:%.2f%%" % (s.getChangePercent()*100))
print(Stock.__doc__)


