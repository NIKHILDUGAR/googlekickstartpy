T = int(input())
for x in range(1, T + 1):
    N = int(input())
    s=input()
    c=[1]
    temp=1
    for i in range(1,len(s)):
       if ord(s[i])>ord(s[i-1]):
           temp+=1
       else:
           temp=1
       c.append(temp)
    print("Case #{}:".format(x),*c,sep=" ")
    
# link https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435a5b/000000000077a882
