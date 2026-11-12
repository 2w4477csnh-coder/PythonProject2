x=int(input())
k=0
for i in range(1,x+1):
    for j in range(i,x+1):
        if i**2+j**2==x:
            k=k+1
print(k)