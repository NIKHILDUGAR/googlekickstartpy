# question link https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201db8/0000000000201c06
T = int(input())
for x in range(1, T + 1):
    N, M = map(int, input().split())
    num=N-M
    den=N+M
    print("Case #{}: {}".format(x, num/den), flush=True)
