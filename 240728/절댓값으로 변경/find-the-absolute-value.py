n=int(input())
a_list=list(map(int,input().split()))

def great(arr):
    for i in range(n):
        if arr[i]<0:
            arr[i]=-arr[i]
        print(arr[i],end=" ")
        
great(a_list)