n=int(input())
q=1
w=1
e=1
for i in range(100,n+1):
    a=i//100
    b=i//10%10
    c=i%10
    q = 1
    for o in range(a):
        q=o*q
    for k in range(b):
        e=k*e
    for l in range(c):
        w=l*w
    if q+w+e==i:
        print(i)
