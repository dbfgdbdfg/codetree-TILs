n=int(input())

a_list= [list(map(int,input().split()))
    for i in range(n)]

sums=0
b_list=[]

for r in range(n):
    for c in range(n-2):
        sums=a_list[r][c]+a_list[r][c+1]+a_list[r][c+2]
    b_list.append(sums)
    sums=0
        
print(max(b_list))