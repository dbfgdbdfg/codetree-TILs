n=int(input())

def great(n):
    if n==0:
        return

    print(n,end=" ")
    great(n-1)
    print(n,end=" ")


great(n)