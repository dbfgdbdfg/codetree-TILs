n,m=map(int,input().split())
a_list=[]
b_list=[]
start=0
for i in range(n):
    w=input().split()
    t,d=int(w[0]),w[1]
    if d=="R":
        for q in range(1,t+1):
            a_list.append(start+q)
        start+=t
    if d=="L":
        for q in range(1,t+1):
            a_list.append(start-q)
        start-=t

start=0        
for i in range(m):
    w=input().split()
    t,d=int(w[0]),w[1]
    if d=="R":
        for q in range(1,t+1):
            b_list.append(start+q)
        start+=t
    if d=="L":
        for q in range(1,t+1):
            b_list.append(start-q)
        start-=t
if len(a_list)>len(b_list):
    for i in range(len(a_list)-len(b_list)):
        b_list.append(b_list[-1])
if len(a_list)<len(b_list):
    for i in range(-len(a_list)+len(b_list)):
        a_list.append(a_list[-1])




nums=0
for i in range(len(a_list)-1):
    if a_list[i]!=b_list[i]:
        if a_list[i+1]==b_list[i+1]:
            nums+=1


print(nums)