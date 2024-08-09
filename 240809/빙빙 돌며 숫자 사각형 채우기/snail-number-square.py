n,m=map(int,input().split())

a_list=[[0]*m for i in range(n)]


dx,dy=[0,1,0,-1],[1,0,-1,0]

dire=0
x,y=0,0
a_list[x][y]=1


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

for i in range(n*m-1):
    nx=x+dx[dire] 
    ny=y+dy[dire]
    if not in_range(nx,ny) or a_list[nx][ny]!=0:
        dire=(dire+1)%4
    x=x+dx[dire]
    y=y+dy[dire]
    a_list[x][y]=i+2



for r in range(n):
    for c in range(m):
        print(a_list[r][c], end=" ")
    print()