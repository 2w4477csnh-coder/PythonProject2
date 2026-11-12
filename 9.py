n, k, r=map(int,input().split())
t=1
while n<r:
    n=((n*k)/100)+n
    t=t+1
print(t)