n=int(input())
a_list=[]
for i in range(n):
    a_list.append(input())

print(a_list)
b_list=[]
nums=1

for i in range(n-1):
    if a_list[i]==a_list[i+1]:
        nums+=1
        b_list.append(nums)
    else:
        nums=1

print(max(b_list))