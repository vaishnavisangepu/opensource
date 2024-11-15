x,n=map(int, input().split())
c_p=100
t_c=x*c_p
p_r=max(n-t_c,0)
print((p_r + c_p-1)//c_p)
