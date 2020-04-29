# question link https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201c0c/0000000000201ca5
    
#FULLY WORKING SOLUTION
    
T = int(input())
for x in range(1, T + 1):
    L, R = map(int, input().split())
    pairs = min(L, R)
    print("Case #{}: {}".format(x, (pairs*(pairs+1))//2, flush=True)) 

#MLE on test set 2 but works on test set 1
def validatee(string):
    k=0
    for i in string:
        if i=="(":
            k+=1
        if i==")":
            k-=1
            if k<0:
                return False
    if k==0:
        return True
    else:return False
T = int(input())
from itertools import combinations
for x in range(1, T + 1):
    L, R = map(int, input().split())
    # s=("("* L) +(")"* R)
    s=""
    while L+R:
        if L==0:
            s+=")"* R
            R=0
        if R==0:
            k="("* L +s
            L=0
            s=k
        else:
            if s=="":
                s+="("
                L-=1
            elif s[-1]=="(":
                s+=")"
                R-=1
            elif s[-1]==")":
                s+="("
                L-=1
    y=0
    res = [s[i: j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]
    for i in res:
        if i[0] != ")" and i[-1] != "(":
            if validatee(i):
                y+=1
    print("Case #{}: {}".format(x, y), flush = True)
