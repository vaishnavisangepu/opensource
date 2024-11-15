v=input().split()
n=int(v[0])
x=int(v[1])
y=int(v[2])
for i in range(n+1):
    if i*x==y:
        print("YES")
        break
        
        
else:
    print("NO")
