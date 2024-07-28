n=int(input())

def great(n):
    if n==0:
        return
    great(n-1)
    print(n,end=" ")
great(n)
print()
def great1(n):
    if n==0:
        return
    print(n,end=" ")
    great1(n-1)
great1(n)