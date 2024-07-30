n=int(input())
a_list=list(map(int,input().split()))

def great(n,arr):
    if n==1:
        return arr[n-1]
    for i in range(n):
        if arr[n-1]<arr[i]:
            return great(n-1,arr)
    return arr[n-1]


print(great(n,a_list))