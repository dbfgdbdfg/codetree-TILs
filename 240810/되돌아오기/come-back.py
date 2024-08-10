n=int(input())
x,y=0,0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
time=0
c=0
a_list=[]

class Great():
    def __init__(self,time,nx,ny):
        self.nx=nx
        self.ny=ny
        self.time=time

for i in range(n):
    w=input().split()
    a,b=w[0],int(w[1])
    if a=="N":
        c=3
        for i in range(b):
            time+=1
            x=x+dx[c]
            y=y+dy[c]
            a_list.append(Great(time,x,y))
    if a=="S":
        c=1
        for i in range(b):
            time+=1
            x=x+dx[c]
            y=y+dy[c]
            a_list.append(Great(time,x,y))
    if a=="W":
        c=2
        for i in range(b):
            time+=1
            x=x+dx[c]
            y=y+dy[c]
            a_list.append(Great(time,x,y))
    if a=="E":
        c=0
        for i in range(b):
            time+=1
            x=x+dx[c]
            y=y+dy[c]
            a_list.append(Great(time,x,y))

found = False
for Great in a_list:
    if Great.nx==0 and Great.ny==0:
        print(Great.time)
        found= True

if not found:
    print("-1")