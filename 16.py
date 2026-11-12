n=int(input())
s=0
for i in range(1,n+1):
    for j in range(1,i):
        if i%j==0:
            s=s+j
    if i==s:
        print(s)
    s=0