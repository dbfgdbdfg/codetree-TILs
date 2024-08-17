n,m=map(int,input().split())

a_list=[list(map(str,input()))
for i in range(n)]
#['T', 'A', 'E', 'H', 'G', 'I']
#['E', 'E', 'L', 'V', 'W', 'E']
#['L', 'E', 'E', 'L', 'S', 'E']
#['H', 'B', 'L', 'U', 'E', 'L']
dx,dy=[0,-1,-1,-1,0,1,1,1],[1,1,0,-1,-1,-1,0,1]
dire=0
nums=0
#오른쪽이 0이고 시계방향으로 회전

def Great(x,y):
    return 0<=x and x<n and 0<=y and y<m

for r in range(n):
    for c in range(m):
        if a_list[r][c]!="L":
            continue
        for i in range(8):
            if Great(r+dx[i],c+dy[i]):
                if a_list[r+dx[i]][c+dy[i]]=="E":
                    dire=i   
                    if Great(r+dx[i]+dx[i],c+dy[i]+dy[i]):
                        if  a_list[r+dx[i]+dx[i]][c+dy[i]+dy[i]]=="E":
                            nums+=1
                            #print(r,c)
      
print(nums)