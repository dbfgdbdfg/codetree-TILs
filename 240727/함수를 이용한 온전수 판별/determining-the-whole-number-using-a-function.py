w=input().split()
a,b=int(w[0]),int(w[1])
def perfect(a):
    if a%2==0:
        return False
    if (a+5)%10==0:
        return False
    if a%3==0 and a%9!=0:
        return False
    return True


nums=0
for i in range(a,b+1):
    if perfect(i):
        nums+=1
print(nums)