w=input().split()
a,b=int(w[0]),int(w[1])

def perfect(n):
    if (n//100+n//10+n%10)%2!=0:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True


nums=0
for i in range(a,b+1):
    if perfect(i):
        nums+=1

print(nums)