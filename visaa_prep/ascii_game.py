s=input()
for char in s:
    if char.islower():
        print(char.upper(),end="")
    else:
        print(char.lower(),end="")
