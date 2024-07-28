n=int(input())

def great(n):
    if n==0:
        return
    great(n-1)
    print("HelloWorld")
great(n)