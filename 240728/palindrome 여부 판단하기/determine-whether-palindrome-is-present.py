a=str(input())

def pail(a):
    return a[::-1]==a

if pail(a):
    print("Yes")
else:
    print("No")