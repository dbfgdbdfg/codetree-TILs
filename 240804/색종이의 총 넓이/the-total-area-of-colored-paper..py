n=int(input())
a_list=[[0]*200 for row in range(200)]

for i in range(n):
    a,b=map(int,input().split())
    for r in range(8):
        for c in range(8):
            a_list[a+r][b+c]=1
nums=0
for row in a_list:
    for element in row:

        nums+=element

print(nums)