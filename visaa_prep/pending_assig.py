n=input().split()
x=int(n[0])
y=int(n[1])
z=int(n[2])
total_time=z*24*60
needed=x*y
if needed<=total_time:
    print("YES")
else:
    print("NO")
