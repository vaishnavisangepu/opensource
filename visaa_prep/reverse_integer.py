n=int(input())
ng=n<0
n=abs(n)
r=int(str(n)[::-1])
if ng:
    r=-r
if r<-2**31 or r>2**31-1:
    r=0
print(r)
