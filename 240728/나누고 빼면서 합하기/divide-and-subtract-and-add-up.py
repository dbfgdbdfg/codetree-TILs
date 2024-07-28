w=input().split()
n,m=int(w[0]),int(w[1])
a_list=list(map(int,input().split()))
sums=0
def great(m,arr):
    global sums
    while m>=1:
        sums+=arr[m-1]
        if m%2==0:
            m=int(m/2)

        elif m%2==1:
            m=m-1

    return sums
print(great(m,a_list))