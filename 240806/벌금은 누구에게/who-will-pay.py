n,m,k=map(int,input().split())
a_list=[]
for i in range(m):
    a_list.append(int(input()))
b_list=[]
c_list=[]
for i in range(1,m):
    b_list=a_list[:i]
    for i in range(1,n+1):
        if b_list.count(i)>=k:
            c_list.append(i)
            
if len(c_list)==0:
    print("-1")
else:
    print(c_list[0])