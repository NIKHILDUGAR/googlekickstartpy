T = int(input())
for x in range(1, T + 1):
    N = int(input())
    c = 0
    S = list(input().split())

    if N == 1:
        print("Case #{}: {}".format(x, 1), flush=True)
        continue
    if N == 2:
        if S[0] != S[1]:
            print("Case #{}: {}".format(x, 1), flush=True)
        else:
            print("Case #{}: {}".format(x, 0), flush=True)
        continue
    k=-1
    if int(S[0]) > int(S[1]):
        c += 1
        k=int(S[0])

    for i in range(len(S)):
        S[i] = int(S[i])
    for i in range(1, len(S) - 1):
        if S[i] > k and S[i] > S[i + 1]:
            c += 1
            k = S[i]
    if S[-1] > max(S[1:len(S) - 1]):
        c += 1
    print("Case #{}: {}".format(x, c), flush=True)
