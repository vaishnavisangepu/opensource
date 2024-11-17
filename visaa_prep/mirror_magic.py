n=int(input())
matrix=[list(map(int, input().split())) for i in range(n)]
m_m=row=[row[::-1] for row in matrix]
for row in m_m:
    print(*row)
