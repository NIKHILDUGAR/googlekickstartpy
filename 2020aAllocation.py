#question link https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d3f56
t=int(input())
for ll in range(t):
    s = str(input())
    tnop=list(s.split(" "))
    snop=int(tnop[1])
    s=str(input())
    l=list(s.split(" "))
    l = [int(i) for i in l]
    l = sorted(l)
    s=0
    c=0
    for i in l:
        if s+i<=snop:
            s=s+i
            c+=1
        else:
            break
    print("Case #"+str(ll+1)+": "+str(c))
