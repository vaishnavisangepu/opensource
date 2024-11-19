N=int(input())
a=list(map(int, input().split()))
max_a=0
c=0
for day in a:
    if day==0:
        c+=1
        if c>max_a:
            max_a=c
    else:
        c=0
print(max_a)
