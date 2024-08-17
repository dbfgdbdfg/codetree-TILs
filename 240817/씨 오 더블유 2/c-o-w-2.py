n=int(input())
a_list=list(map(str,input()))
nums=0
#['C', 'O', 'O', 'W', 'W', 'W']
for i in range(n-2):
    if a_list[i]=="C":
        for q in range(i+1,n):
            if a_list[q]=="O":
                for w in range(q+1,n):
                    if a_list[w]=="W":
                        nums+=1
print(nums)