w=input().split()
a,b=int(w[0]),int(w[1])
nums=0

def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True




for i in range(a,b+1):
    if i==1:
        nums+=0
    elif prime(i):
        nums+=i
print(nums)