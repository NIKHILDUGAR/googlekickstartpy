#works on test case1, TLE on case 2. question link https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050eda/0000000000119866
T = int(input())
for x in range(1, T + 1):
    N, Q = map(int, input().split())
    S = input()
    L=[char for char in S]
    y=0
    for i in range(Q):
        s1,e1= map(int, input().split())
        listt=[]
        sr=L[s1-1:e1]
        for i in range(len(sr)):
            if (sr[i] in listt):
                listt.remove(sr[i])
            else:
                listt.append(sr[i])
        if (len(sr) % 2 == 0 and len(listt) == 0 ) or (len(sr) % 2 == 1 and len(listt) == 1):
            y+=1
    print("Case #{}: {}".format(x, y),flush=True)
