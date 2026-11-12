n=int(input())
for i in range(2,n+1):
    k=0
    for r in range(2,i):
        if r*r>i:
            break
        if i%r==0:
            k=1
            break
    if k==0:
        print(i)
