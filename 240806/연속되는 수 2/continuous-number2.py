n=int(input())
a_list=[]
for i in range(n):
    a_list.append(input())


b_list=[]
nums=1

for i in range(n-1):
    if a_list[i]==a_list[i+1]:
        nums+=1
        b_list.append(nums)
    else:
        nums=1
if len(b_list)=0:
    print("0")
else:

    print(max(b_list))