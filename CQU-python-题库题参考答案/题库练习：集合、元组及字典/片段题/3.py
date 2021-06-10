<<<<<<< HEAD
item = input() or "None"
goods = {}
while(item !="None"):
    name, cost = item.split()
    cost = eval(cost)
    goods[name] = cost
    item = input() or "None"

goodsNum =len(goods)

money=0
for i in goods:
    money += goods[i]


=======
item = input() or "None"
goods = {}
while(item !="None"):
    name, cost = item.split()
    cost = eval(cost)
    goods[name] = cost
    item = input() or "None"

goodsNum =len(goods)

money=0
for i in goods:
    money += goods[i]


>>>>>>> 91c5edef37c527a60ab0cadc28e08bc788a52119
print(goodsNum,"%.2f"%(money))

