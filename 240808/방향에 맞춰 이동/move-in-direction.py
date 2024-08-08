n=int(input())
x=0
y=0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

for i in range(n):
    w=input().split()
    a,b=w[0],int(w[1])
    c=0
    if a=="N":
        c=3
    elif a=="S":
        c=1
    elif a=="w":
        c=2
    
    x=x+dx[c]*b
    y=y+dy[c]*b


print(x,y)