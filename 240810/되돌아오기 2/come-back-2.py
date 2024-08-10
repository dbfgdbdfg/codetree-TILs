n=str(input())

x,y=0,0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
nums=3

a_list=[]

class Great():
    def __init__(self,time,nx,ny):
        self.nx=nx
        self.ny=ny
        self.time=time

for i in range(len(n)):
    if n[i]=="L":
        nums-=1
    elif n[i]=="R":
        nums+=1
    elif n[i]=="F":
        x+=dx[nums%4]
        y+=dy[nums%4]
    a_list.append(Great(i+1,x,y))


found = False
for Great in a_list:
    if Great.nx==0 and Great.ny==0:
        print(Great.time)
        found = True
        break
if not found:
    print("-1")