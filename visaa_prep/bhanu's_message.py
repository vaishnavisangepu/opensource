n=input()
if n.startswith('+') and len(n)==14:
    c_c=n[1:3]
    a_n=n[4:]
    if c_c.isdigit() and a_n.isdigit() and n[3]==' ':
        print("Correct")
    else:
        print("Incorrect")
else:
    print("Incorrect")
