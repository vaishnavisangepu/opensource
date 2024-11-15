m=int(input())
if m<1 or m>12:
    print("Invalid")
elif m in [3,4,5]:
    print("Spring")
elif m in [6,7,8]:
    print("Summer")
elif m in [9,10,11]:
    print("Autumn")
else:
    print("Winter")
    
