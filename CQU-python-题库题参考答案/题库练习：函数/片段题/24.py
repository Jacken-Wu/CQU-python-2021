def play_card(cards):
    cards.sort() #排序，每一次找连牌从最小的点数开始
    for start in range(len(cards)): #遍历cards的每一个元素（都有可能成为连牌的第一张）
        now=cards[start]  #把start位置的牌设为连牌的开始
        count=1  #连牌张数计数
        seq=[now]  #存放连牌的列表
        while True:       #寻找start位置的牌为起始的连牌
            if now+1 in cards:  
                count += 1
                now += 1
                seq.append(now)
    #更新count,now和seq
            else:
                break
    #连牌中断，下一个start
        if count>=5:  #如果连牌张数大于5
            return seq
                          
origin=input().split()
origin=[eval(x) for x in origin]
result=play_card(origin)
for x in result:
    print(x,end=" ")

