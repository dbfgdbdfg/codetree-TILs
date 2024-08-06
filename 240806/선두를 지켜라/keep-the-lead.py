n,m=map(int,input().split())
a_list=[]
b_list=[]
start=0
time=0
for i in range(n):
    v,t=map(int,input().split())
    time+=t
    for i in range(t):
        start+=v
        a_list.append(start)

start=0
for i in range(m):
    v,t=map(int,input().split())
    for i in range(t):
        start+=v
        b_list.append(start)
#print(a_list,b_list)

c_list=[]
nums=0
for i in range(time):
    if (a_list[i]-b_list[i])!=0:
        c_list.append(a_list[i]-b_list[i])
for i in range(len(c_list)-1):
    if c_list[i]*c_list[i+1]<0:
        nums+=1
#print(c_list)
print(nums)