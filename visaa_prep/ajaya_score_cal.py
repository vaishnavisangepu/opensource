T=int(input())
t_c=[tuple(map(int,input().split())) for _ in range(T)]
for x,n in t_c:
    print((x//10) *n)
