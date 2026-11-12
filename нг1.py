n=input()
s=0
for i in n:
    f=int(i)**len(n)
    s=s+f
if s==int(n):
    print("YES")
else:
    print("NO")

