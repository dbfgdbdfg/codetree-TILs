n=int(input())
a_list=list(map(int,input().split()))


def what(arr):
    for i in range(n):
        if arr[i]%2==0:
            arr[i]=arr[i]/2

what(a_list)           
for  i in a_list:
    print(int(i),end=" ")