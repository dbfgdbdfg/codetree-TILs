n,m=map(int,input().split())
a_list=[]
b_list=[]
start=0
sums=0

for i in range(n):
    w=input().split()
    x,y=w[0],int(w[1])
    sums+=y
    if x=="R":
        for q in range(1,y+1):
            a_list.append(start+q)
        start+=y
    if x=="L":
        for q in range(1,y+1):
            a_list.append(start-q)
        start-=y
start=0
for i in range(m):
    w=input().split()
    x,y=w[0],int(w[1])
    if x=="R":
        for q in range(1,y+1):
            b_list.append(start+q)
        start+=y
    if x=="L":
        for q in range(1,y+1):
            b_list.append(start-q)
        start-=y



time=0
while time<=sums:
    if time==sums:
        print("-1")
    if a_list[time]==b_list[time]:
        print(time+1)
        break
    time+=1