n=int(input())

a_list=list(map(int,input().split()))
a_list.sort()

b_list=[]
for i in range(n*2):
    b_list.append(a_list[i]+a_list[n*2-1-i])

print(max(b_list))