n=int(input())

def great(n):
    if n==1:
        return 2
    if n==2:
        return 4
    return (great(n-2)*great(n-1))%100

print(great(n))