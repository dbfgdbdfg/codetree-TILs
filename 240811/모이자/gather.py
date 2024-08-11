n=int(input())
w=input().split()

a_list=[]
nums=0
for i in range(n):
    for c in range(n):
        nums+=int(w[c])*abs(i-c)
    a_list.append(nums)
    nums=0

    
print(min(a_list))