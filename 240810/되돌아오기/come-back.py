n=int(input())
x,y=0,0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
time=0
c=0
while True:
    for i in range(n):
        w=input().split()
        a,b=w[0],int(w[1])
        if a=="N":
            c=3
            for i in range(b):
                time+=1
                x=x+dx[c]
                y=y+dy[c]
                if x==0 and y==0:
                    print(time)
                    break
        if a=="S":
            c=1
            for i in range(b):
                time+=1
                x=x+dx[c]
                y=y+dy[c]
                if x==0 and y==0:
                    print(time)
                    break
   
        if a=="W":
            c=2
            for i in range(b):
                time+=1
                x=x+dx[c]
                y=y+dy[c]
                if x==0 and y==0:
                    print(time)
                    return False
                    
        if a=="E":
            c=0
            for i in range(b):
                time+=1
                x=x+dx[c]
                y=y+dy[c]
                if x==0 and y==0:
                    print(time)
                    break

if False:
    print("-1")