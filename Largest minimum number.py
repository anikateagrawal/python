n,c=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
from itertools import combinations
l=list(combinations(l,c))
print(l)
d=[]
for i in l:
    ll=[]
    for j in range(len(i)-1):
        ll.append(i[j+1]-i[j])
    d.append(min(ll))
print(max(d))
