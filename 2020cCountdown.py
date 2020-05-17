# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff43/00000000003380d2
T = int(input())
for x in range(1, T + 1):
    N, P = map(int, input().split())
    g=[]
    for i in range(1,P+1):
        g.append(i)
    g=g[::-1]
    S = list(input().split())
    c=0
    l=[int(i) for i in S]
    if P==1:
        c=l.count(1)
    else:
        for i in range(len(l)-P+1):
            if l[i]==g[0]:
                if l[i+1]==g[1]:
                    if l[i+1:i+P]==g[1:]:
                        c+=1
    print("Case #{}: {}".format(x, c), flush=True)
