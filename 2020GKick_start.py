#link- https://codingcompetitions.withgoogle.com/kickstart/round/00000000001a0069/0000000000414bfb
# no TLE ,Working soln
t=input()
for i in range(int(t)):
    x=input()
    s1=4
    s2=5
    sub1=x[0:4]
    sub2=x[0:5]
    kick=0
    k1=0
    if sub1 == "KICK":
        k1+=1
    if sub2 == "START":
        kick+=k1
    for j in range(len(x)-5):
        sub1=sub1[1:]+x[s1]
        sub2=sub2[1:]+x[s2]
        if sub1 == "KICK":
            k1+=1
        if sub2 == "START":
            kick+=k1
        s1+=1
        s2+=1
    print("Case #"+str(int(i)+1)+ ": "+str(kick) )
    
    
#Regex soln that gave TLE
import re
T = int(input())
for x in range(1, T + 1):
    N = input()
    l=[m.start() for m in re.finditer('START', N)]
    curr=0
    j=[i for i in range(len(N)-3) if "KICK" == N[i:i+4]]
    for i in l:
        for k in j:
            if k<i:
                curr+=1
            else:
                break
    print("Case #{}: {}".format(x, curr), flush=True)
        
