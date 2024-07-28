w=input().split()
a,b=int(w[0]),int(w[1])

def what(n,m):
    if n>m:
        n*=2
        m+=10
    elif n<m:
        n+=10
        m*=2
    return n,m

a,b=what(a,b)
print(a,b)