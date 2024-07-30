n=int(input())

def great(n):
    if n==1:
        return 1
    if n==2:
        return 2
    if n%2==0:
        return great(n-2)+n
    else:
        return great(n-2)+n

print(great(n))