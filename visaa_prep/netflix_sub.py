input_val=input().split()
a=int(input_val[0])
b=int(input_val[1])
c=int(input_val[2])
x=int(input_val[3])
if a+b>=x or a+c>=x or b+c>=x:
    print("YES")
else:
    print("NO")
