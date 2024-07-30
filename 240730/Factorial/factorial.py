n=int(input())

def great(n):
    if n==1:
        return 1
    return great(n-1)*n
print(great(n))