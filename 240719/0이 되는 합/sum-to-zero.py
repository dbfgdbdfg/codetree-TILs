n=int(input())
w=input().split()
nums=0
for i in range(0,n):
    for q in range(i+1,n):
        for e in range(q+1,n):
            if int(w[i])+int(w[q])+int(w[e])==0:
                nums+=1

print(nums)