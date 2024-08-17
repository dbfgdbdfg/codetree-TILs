n,h,t=map(int,input().split())

a_list=list(map(int,input().split()))

cost=0
cost_list=[]

for i in range(n-t+1):
    for q in range(t):
        cost=cost+abs(a_list[i+q]-h)

    cost_list.append(cost)

    cost=0

print(min(cost_list))