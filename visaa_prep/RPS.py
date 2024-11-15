n=input().split()
v_t=n[0]
c_t=n[1]
if v_t==c_t:
    print("NULL")
elif(v_t=='R' and c_t=='S') or (v_t=='P' and c_t=='R') or (v_t=='S' and c_t=='P'):
    print("Vignesh")
else:
    print("Charan")
