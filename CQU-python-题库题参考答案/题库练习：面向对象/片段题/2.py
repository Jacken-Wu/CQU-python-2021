class User:
    def __init__(self, first_name, last_name, tel, place):
        #完成成员变量的赋值
        self.first_name = first_name
        self.last_name = last_name
        self.tel = tel
        self.place = place

    def describe_user(self):
        print(self.first_name + self.last_name + " tel:{},place:{}".format(self.tel, self.place))
s = input().split(",")
u1 = User(s[0], s[1], s[2], s[3])
u1.describe_user()



