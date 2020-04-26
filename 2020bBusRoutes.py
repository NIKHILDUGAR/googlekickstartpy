# question link https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d83bf
T=int(input())
for x in range(1, T + 1):
    N, D = map(int, input().split())
    S = [int(x) for x in input().split()]
    for i in S[::-1]:
        P=D//i
        D=P*i
    print("Case #{}: {}".format(x, D), flush = True)
