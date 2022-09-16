M = int(input())
numbers = list(map(int,input().split()))
a = set()
goodpairs = []
for i in numbers:
    a.add(i)
for el in a:
    if M - el in a:
        goodpairs.append([el,M-el])
for el in goodpairs:
    el1,el2 = el
    if el1 > el2:
        print(el1,'and',el2)