#question link https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050e01/00000000000698d6 didn't participate but felt like a fun problem to try
from itertools import combinations  as comb
t=int(input())
for ll in range(t):
    tnop=list(input())
    snop=int(tnop[2])
    s=str(input())
    l=list(s.split(" "))
    g=set(comb(l,snop))
    m=100000
    for i in g:
        s=0
        for k in i:
            s+=abs(int(max(i))-int(k))
        m=min(s,m)
    print("Case #"+str(ll+1)+": "+str(m))
