n=int(input())
a_list=[[0]*n for i in range(n)]
dx,dy=[0,-1,0,1],[1,0,-1,0]
x,y=n-1,n-1
dire=3

def Great(r,c,dire):
    if (0<=r<n and  0<=c<n) and a_list[r][c]==0:
        return dire
    else:
        dire=(dire+3)%4
        return dire
    


for i in range(n**2,0,-1):  
    a_list[x][y]=i
    nx=x+dx[dire]
    ny=y+dy[dire]
    dire=Great(nx,ny,dire)
    x=x+dx[dire]
    y=y+dy[dire]


for row in a_list:
    for element in row:
        print(element,end=" ")
    print()