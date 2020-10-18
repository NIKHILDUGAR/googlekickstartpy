# link - https://codingcompetitions.withgoogle.com/kickstart/round/00000000001a0069/0000000000414a23
T = int(input())
for x in range(1, T + 1):
    R = int(input())
    matrix = []
    for i in range(R):
        a=(input().split())
        for i in range(len(a)):
            a[i]=int(a[i])
        matrix.append(a)
    k=0
    for ite in range(R):
        s=0
        for i in range(R):
            try:
                s+=matrix[ite+i][i]
            except:
                continue
        k=max(k,s)
    for ite in range(R):
        s=0
        for i in range(R):
            try:
                s+=matrix[i][i+ite]
            except:
                continue
        k=max(k,s)
    print("Case #{}: {}".format(x, k), flush=True)
