# the question link https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d82e6

T = int(input())#input of number of test cases
for x in range(1, T + 1):
    n=int(input())#no of entries
    s = str(input())#input of entries
    c=0
    tnop = list(s.split(" "))#conversion of entries to list
    for i in range(1,len(tnop)-1):
        if int(tnop[i])>int(tnop[i-1]) and int(tnop[i])>int(tnop[i+1]):#checking of the strictly greater than condition
            c+=1
    print("Case #{}: {}".format(x, c), flush=True)
