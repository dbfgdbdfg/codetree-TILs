n=int(input())
a_list=[
    list(map(int,input().split()))
    for i in range(n)]
nums=0

for r in range(n):
    for c in range(n):
        b_list=[]
        if r-1>=0:
            b_list.append(a_list[r-1][c])
        if c-1>=0:
            b_list.append(a_list[r][c-1])
        if r+1<n:
            b_list.append(a_list[r+1][c])
        if c+1<n:
            b_list.append(a_list[r][c+1])
        
        num=b_list.count(1)
 
        if num>=3:
            nums+=1

print(nums)









'''
x, y = 2, 4
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]


def in_range(x, y):
    return 0 <= x and x < 5 and 0 <= y and y < 5


cnt = 0
for dx, dy in zip(dxs, dys):
    nx, ny = x + dx, y + dy
    if in_range(nx, ny) and a[nx][ny] == 1:
        cnt += 1

print(cnt)

>> 1
'''