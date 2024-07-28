n=int(input())

def great(n):
    if n==0:
        return 0
    return great(n-1)+n

print(great(n))