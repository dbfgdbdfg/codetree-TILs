a_list=list(map(str,input()))
n=len(a_list)
#[')', '(', '(', '(', ')', '(', ')', ')', '(', ')', ')']
nums=0

for i in range(n-1):
    if a_list[i]=='(' and a_list[i+1]=='(':
        for q in range(i+1,n-1):
            if a_list[q]==')' and a_list[q+1]==')':
                nums+=1
print(nums)