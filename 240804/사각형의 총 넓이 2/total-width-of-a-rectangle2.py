n=int(input())
a_list = [[0]*200 for i in range (200)]


for i in range(n):
    w=input().split()
    x1,y1,x2,y2=int(w[0]),int(w[1]),int(w[2]),int(w[3])
    for r in range(x1+100,x2+100): 
        for c in range(y1+100,y2+100):
            a_list[r][c]=1
          
sums=0

for row in a_list:
    for element in row:
        sums+=element

print(sums)