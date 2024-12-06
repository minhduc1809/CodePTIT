from itertools import combinations
n,m=map(int,input().split())
s=list(map(int,input().split()))
a=set()
for i in s:
    a.add(i)
c=sorted(a)
b=list(combinations(c,m))
for i in b:
    for j in i:
        print(j,end=" ")
    print()