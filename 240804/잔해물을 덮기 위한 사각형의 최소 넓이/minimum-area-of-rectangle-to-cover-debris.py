a_list=[[0]*2001 for row in range(2001)]
nums=0
x1,y1,x2,y2=map(int,input().split())
for r in range(x1+1000,x2+1000):
    for c in range(y1+1000,y2+1000):
        a_list[r][c]=1

x11,y11,x22,y22=map(int,input().split())
for r in range(x11+1000,x22+1000):
    for c in range(y11+1000,y22+1000):
        a_list[r][c]=0

if (y2>y22 and x1<x11) or (x22<x2 and y11>y1) or x2<=x11 or y2<=y11 or x1>x22 or y1>y22:
    print((x2-x1)*(y2-y1))
else:
    for row in a_list:
        for element in row:
            nums+=element
    print(nums)