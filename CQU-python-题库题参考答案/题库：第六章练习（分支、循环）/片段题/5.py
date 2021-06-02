def binarySearch(s,v):
    begin,end = 0, len(s)-1
    while begin <= end:

        mid = (begin+end)//2
        if s[mid] == v:
            print("Found:%d" % mid)
            break
        elif v > s[mid]:
            begin = mid + 1

        else:
            end = mid - 1
    else:
        print("Not found")

a = [1,3, 12, 45, 66, 89, 123, 154, 768, 9921]
v = int(input())
binarySearch(a,v)



