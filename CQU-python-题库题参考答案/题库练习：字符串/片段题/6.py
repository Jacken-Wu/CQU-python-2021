def main():
    somestr,substr,startstr,endstr=input().split()
    startnum=int(startstr)
    endnum=int(endstr)
    fun(somestr, substr, startnum, endnum)

def fun(somestr,substr,startnum,endnum):
    l = []
    while startnum < endnum:
        if somestr[startnum: startnum+3] == substr:
            l.append(str(startnum))
            startnum += 2
        startnum += 1
    if l:
        print(','.join(l))
    else:
        print('none')


main()




