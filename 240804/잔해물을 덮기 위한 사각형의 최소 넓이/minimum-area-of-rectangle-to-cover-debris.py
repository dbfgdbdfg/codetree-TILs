a_list=[[0]*2000 for row in range(2000)]

x1,y1,x2,y2=map(int,input().split())

for r in range(x1+1000,x2+1000):
    for c in range(y1+1000,y2+1000):
        a_list[r][c]=1

x11,y11,x22,y22=map(int,input().split())

for r in range(x11+1000,x22+1000):
    for c in range(y11+1000,y22+1000):
        a_list[r][c]=0

while True:
    if a_list[x1+1000][y1+1000]==1:
        a=x1
        b=y1
        break
    x1+=1
    if a_list[x1+1000][y1+1000]==1:
        a=x1
        b=y1
        break
    x1-=1
    y1+=1

while True:
    if a_list[x2+1000][y2+1000]==1:
        c=x2
        d=y2
        break
    x2-=1
    if a_list[x2+1000][y2+1000]==1:
        c=x2
        d=y2
        break
    x2+=1
    y2-=1    
    
print((c-a+1)*(d-b+1))