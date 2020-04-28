# question link - https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201ca2/0000000000201d30
T = int(input())
for x in range(1, T + 1):
    N = int(input())
    l=[]
    m=0
    curr=None
    for i in range(N):
        S =str(input())
        l.append(S)
    l = sorted(l)
    for i in l:
        j=i
        i = "".join(i.split())
        k=set(i)
        if len(k)>m:
            m=len(k)
            curr=j
    print("Case #{}: {}".format(x, curr), flush = True)
