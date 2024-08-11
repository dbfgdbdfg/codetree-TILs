n=int(input())

a_list= [list(map(int,input().split()))
    for i in range(n)]

sums=0
b_list=[]

for c in range(n):
    for r in range(n-2):
        sums+=a_list[r][c]
    b_list.append(sums)
    sums=0
        
print(max(b_list))