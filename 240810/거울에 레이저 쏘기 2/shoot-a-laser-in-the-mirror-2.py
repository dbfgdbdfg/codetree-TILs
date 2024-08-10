n=int(input())
x,y=0,0
a_list=[list(input())
    for i in range(n)]
# / 는 하나로 \는 \\로 입력됬다

global dire
dire=0
#아래로 0 오른쪽 1 위로 2 왼쪽 3
dx,dy=[-1,0,1,0],[0,1,0,-1]

m=int(input())
if m//n==0:
    x=0
    y=m-1
    dire=0
elif m//n==1:
    x=m%n-1
    y=n-1
    dire=3
elif m//n==2:
    x=n-1
    y=n-m%n
    dire=2
elif m//n==3:
    x=n-m%n
    y=0
    dire =1
#m을 이용해서 시작 좌표 생성
#print(a_list)
#print(x,y,dire)

ting=0

def Great(n):
    if n==3:
        n=2
    if n==2:
        n=3
    if n==1:
        n=0
    if n==0:
        n=1
def Fant(n):
    if n==0:
        n=3
    if n==3:
        n=0
    if n==1:
        n=2
    if n==2:
        n=1
#아래로 0 오른쪽 1 위로 2 왼쪽 3



while True:
    if a_list[x][y]=='\\':
        Great(dire)
        ting+=1
        x=x+dx[dire]
        y=y+dy[dire]

    if a_list[x][y]=="/":
        Fant(dire)
        ting+=1
        x=x+dx[dire]
        y=y+dy[dire]
    if x<0 or y<0 or x>=n or y>=n:
        print(ting)
        break