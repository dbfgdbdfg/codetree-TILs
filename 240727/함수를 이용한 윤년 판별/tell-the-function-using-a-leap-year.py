def yune(n):
    if n%4!=0:
        return False
    if n%100==0 and n%400!=0:
        return False
    return True

a=int(input())
if yune(a):
    print("true")
else:
    print("false")