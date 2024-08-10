n,m=map(int,input().split())
a_list=[[0]*n for i in range(n)]
c=0
def comfort(a,b):
    if c==3:
        return 1
    else:
        return 0

def Great(a,b):
    global c
    c=0
    if a-1>0 and a_list[a-2][b-1]==1:
        c+=1
    if b-1>0 and a_list[a-1][b-2]==1:
        c+=1
    if b+1<=n and a_list[a-1][b]==1:
        c+=1
    if a+1<=n and a_list[a][b-1]==1:
        c+=1
    print(comfort(a,b))
 


for i in range(m):
    x,y=map(int,input().split())
    a_list[x-1][y-1]=1
    Great(x,y)