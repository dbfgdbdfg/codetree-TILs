w=input().split()
m,d=int(w[0]),int(w[1])
a_list=[0,31,28,31,30,31,30,31,31,30,31,30,31]

def right(a,b):
    if a>12:
        return False
    if a<13 and int(a_list[a])<b:
        return False
    return True

if right(m,d):
    print("Yes")
else:
    print("No")