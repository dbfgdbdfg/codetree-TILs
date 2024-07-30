n=int(input())

def great(n):
    nums=0
    while n!=1:
        if n%2==0:
            n=int(n/2)
            nums+=1
        else:
            n=n//3
            nums+=1
    return nums
print(great(n))