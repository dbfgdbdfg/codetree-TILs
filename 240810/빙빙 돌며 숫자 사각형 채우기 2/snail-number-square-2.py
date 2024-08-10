n,m=map(int,input().split())

a_list=[[0]*m for i in range(n)]

r,c=0,0
dx,dy=[1,0,-1,0],[0,1,0,-1]

dire=0

def Great(a,b,dire):
    if (0<=a<n and 0<=b<m) and a_list[a][b]==0:
        return dire
    else:
        dire=(dire+1)%4
        return dire


for i in range(1,n*m+1):
    a_list[r][c]=i
    nr=r+dx[dire]
    nc=c+dy[dire]
    #print(r,c,i,dire,nr,nc,"d")
    dire=Great(nr,nc,dire)
    r=r+dx[dire]
    c=c+dy[dire]








for row in a_list:
    for element in row:
        print(element,end=" ")
    print()