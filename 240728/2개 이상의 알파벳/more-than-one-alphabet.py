a=str(input())
a_set={}

def great(n):
    for i in range(len(n)):
        a_set.add(n[i])
    if len(a_set)>1:
        return True
if great(a):
    print("Yes")
else:
    print("No")