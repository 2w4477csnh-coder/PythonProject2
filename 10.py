a=float(input())
k=0
while True:
    if a==0:
        break
    else:
        b=float(input())
        if b==0:
            break
        if b<a:
            k=k+1
        a=b
print(k)
