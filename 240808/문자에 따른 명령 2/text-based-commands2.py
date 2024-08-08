x,y=0,0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
nums=3
n=str(input())
for i in range(len(n)):
    if n[i]=="L":
        nums-=1
    elif n[i]=="R":
        nums+=1
    elif n[i]=="F":
        x+=dx[nums%4]
        y+=dy[nums%4]
print(x,y)








dir_num = 3 
x, y = 1, 5
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

# rotate direction
dir_num = (dir_num + 1) % 4

# move
nx, ny = x + dx[dir_num], y + dy[dir_num]