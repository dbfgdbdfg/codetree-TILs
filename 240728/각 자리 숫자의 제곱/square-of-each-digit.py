n=int(input())

def great(n):
    if n<10:
        return n**2

    return great(n//10) + (n%10)**2

print(great(n))