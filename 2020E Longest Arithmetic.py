# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff47/00000000003bf4ed#problem
T = int(input())
for x in range(1, T + 1):
    N = int(input())
    S = list(map(int, input().split()))
    l=[]
    for i in range(len(S)-1):
        l.append(S[i+1]-S[i])
    ans, temp = 1, 1
    n=len(l)
    for i in range(1, n):
        if l[i] == l[i - 1]:
            temp = temp + 1
        else:
            ans = max(ans, temp)
            temp = 1
    c = max(ans, temp)+1
    print("Case #{}: {}".format(x, c), flush=True)
