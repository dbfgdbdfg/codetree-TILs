w=input().split()
a,b,c=int(w[0]),int(w[1]),int(w[2])

def great(a,b,c):
    return nums(a*b*c)

def nums(n):
    if n//10==0:
        return n
    return nums(n//10)+n%10


print(great(a,b,c))