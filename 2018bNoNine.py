
# The following solution faces TLE. question link https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050ff4/0000000000051183
T = int(input())
for x in range(1, T + 1):
    N, P = map(int, input().split())
    c=0
    for i in range(N,P+1):
        if i%9!=0:
            if str(i).count('9')==0:
                c+=1
    print("Case #{}: {}".format(x, c), flush=True)
