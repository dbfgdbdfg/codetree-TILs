n=int(input())
a_list = [[0]*10 for i in range (10)]


for i in range(n):
    w=input().split()
    x1,y1,x2,y2=int(w[0]),int(w[1]),int(w[2]),int(w[3])
    for r in range(x1,x2): 
        for c in range(y1,y2):
            a_list[r][c]=1
          
sums=0

for row in a_list:
    for element in row:
        sums+=element

print(sums)