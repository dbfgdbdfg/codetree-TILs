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
x_list=[]
y_list=[]



for r in range(x1+1000,x2+1000):
    for c in range(y1+1000,y2+1000):
        if a_list[r][c]==1:
            x_list.append(r-1000)
            y_list.append(c-1000)

if len(x_list)>0 and len(y_list)>0 :

    print((max(x_list)-min(x_list) +1)*(max(y_list)-min(y_list)+1))
else:
    print("0")