a=str(input())

nums=0
for i in range(len(a)):
    if a[i]=="(":
        for c in range(i,len(a)):
            if a[c]==")":
                nums+=1

print(nums)