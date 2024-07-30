n=int(input())
a=1
def great(n):
    if n==1:
        return 1
    if n==2:
        return 1
    return great(n-1)+great(n-2)

print(great(n))