import datetime


class Ticket:
    def __init__(self, adult, kid, date):
        self.adult = adult
        self.kid = kid
        self.date = date

    def weekend(self):
        if datetime.datetime.strptime(self.date, '%Y-%m-%d').strftime('%w') in ['0', '6']:
            return True
        return False

    def cost(self, w):
        if w:
            return self.adult * 120 + self.kid * 60
        return self.adult * 100 + self.kid * 50


l = input().split(',')
t = Ticket(int(l[0]), int(l[1]), l[2])
f = t.weekend()
print('adult:%d,child:%d,isWeekend:%s,total cost:%.1f' % (t.adult, t.kid, f, t.cost(f)))

