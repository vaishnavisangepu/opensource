n=int(input())
arr=list(map(int, input().split()))
u=[]
s=set()
for ele in arr:
    if ele not in s:
        u.append(ele)
        s.add(ele)
print(" ".join(map(str, u)))
