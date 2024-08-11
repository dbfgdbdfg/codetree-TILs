n,t=map(int,input().split())
tts=str(input())
a_list=[list(map(int,input().split()))
    for i in range(n)]
sums=0
dx,dy=[-1,0,1,0],[0,1,0,-1]
dire=0
x,y=(n-1)//2,(n-2)//2

for i in range(t):
    

    if tts[i]=="L":
        dire=(dire+3)%4
    elif tts[i]=="R":
        dire=(dire+1)%4
    elif tts[i]=="F":
        nx=x+dx[dire]
        ny=y+dy[dire]
        if 0<=nx<n and 0<=ny<n:
            sums+=a_list[nx][ny]
            x=nx
            y=ny
        else:
            sums+=0

print(sums)