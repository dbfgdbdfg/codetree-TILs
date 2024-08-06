n,t=map(int,input().split())
a_list=[]

a_list=list(map(int,input().split()))
nums=1
b_list=[]


if n==1:
    if a_list[0]<=t:
        print("0")
    else:
        print("1")
else:
    for i in range(n-1):
        if a_list[i]>t:
            if a_list[i]<a_list[i+1]:
                nums+=1
                b_list.append(nums)
            else:
                nums=1
                b_list.append(nums)
        else:
            b_list.append(0)
    print(max(b_list))