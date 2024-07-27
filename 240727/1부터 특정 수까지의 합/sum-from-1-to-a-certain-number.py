n=int(input())

def dive(a):
    sums=0
    for i in range(1,a+1):
        sums+=i
    
    return sums//10
print(dive(n))