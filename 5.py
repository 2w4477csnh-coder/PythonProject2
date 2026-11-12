n=int(input())
s=1
st=''
while s**3<=n:
    st=st+str(s**3)+' '
    s=s+1
print(st)

