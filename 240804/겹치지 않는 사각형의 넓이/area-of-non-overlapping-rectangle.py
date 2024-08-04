a_list=[[0]*2000 for row in range(2000)]

for i in range(2):
    x1,y1,x2,y2=map(int,input().split())
    for r in range(x1+1000,x2+1000):
        for c in range(y1+1000,y2+1000):
            a_list[r][c]=1

a1,b1,a2,b2=map(int,input().split())
for r in range(a1+1000,a2+1000):
        for c in range(b1+1000,b2+1000):
            a_list[r][c]=0
nums=0
for row in a_list:
    for element in row:
        nums+=element
print(nums)