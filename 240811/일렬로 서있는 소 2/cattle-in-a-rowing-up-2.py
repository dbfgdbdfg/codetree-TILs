n=int(input())
nums=0
w=input().split()

for i in range(n):
    for j in range(i,n):
        for k in range(j,n):
            if (int(w[i])<=int(w[j])<=int(w[k])) and i<j<k :   
                nums+=1
print(nums)