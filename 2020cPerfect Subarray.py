# THIS SOLUTION GIVES TLE.
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff43/00000000003381cb
T = int(input())
for x in range(1, T + 1):
    N = int(input())
    A = list(map(int,input().split()))
    count=0
    for i in range(0,N):
        temp = 0
        for j in range(i,N):
            temp += A[j]
            if temp>=0:
                if (temp**0.5).is_integer():
                    count += 1
    print("Case #{}: {}".format(x, count), flush=True)
