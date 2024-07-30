n=int(input())
nums=0
def great(n):
    global nums
    if n==1:
        return nums
    elif n%2==0:
        nums+=1
        return great(n/2)
    elif n%2==1:
        nums+=1
        return great(n*3+1)
print(great(n))