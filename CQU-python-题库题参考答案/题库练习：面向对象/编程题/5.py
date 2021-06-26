class Money:
    def __init__(self, m, y, years):
        self.money = m
        self.m = y / 1200
        self.month = years * 12

    def pay(self):
        monthly_payment = (self.money * self.m * (1 + self.m)**self.month) / ((1 + self.m)**self.month - 1)
        total = self.month * monthly_payment - self.money
        return monthly_payment, total


l = eval(input())
money = Money(l[0], l[1], l[2])
print('monthly_payment: %.2f, Total interest: %.2f' % money.pay())

