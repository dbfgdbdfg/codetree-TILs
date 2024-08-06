n=int(input())
a_list=[[0]*201 for row in range(201)]

for i in range(1,n+1):
    x1,y1,x2,y2=map(int,input().split())
    if i%2==1:
        for r in range(x1,x2):
            for c in range(y1,y2):
                a_list[r][c]=1
    if i%2==0:
        for r in range(x1,x2):
            for c in range(y1,y2):
                a_list[r][c]=2
#빨강은 1 파랑은 2

nums=0
for row in a_list:
    for element in row:
        if element==2:
            nums+=1
print(nums)