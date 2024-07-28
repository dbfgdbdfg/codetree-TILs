n=int(input())
a_list=list(map(int,input().split()))


def what(arr):
    for i in arr:
        if i%2==0:
            arr[arr.index(i)]=i/2

what(a_list)           
for  i in a_list:
    print(int(i),end=" ")