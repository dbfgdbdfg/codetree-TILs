n=int(input())
a_list=[]
for i in range(n):
    a_list.append(int(input()))
nums=1
b_list=[]

if n==1:
    print("1")
else:


    for i in range(n-1):
        if a_list[i]*a_list[i-1]>0:
            nums+=1
            b_list.append(nums)
        else:
            nums=1
            b_list.append(nums)
    print(max(b_list))