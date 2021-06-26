#创建Person类
class Person:

    count = 0
    def show(self, name):
        self.name = name
        print(self.name,"test!!!")
p1 = Person()
#输入name变量
name=input()
print(p1.count)
#调用show方法完成输出
p1.show(name)



