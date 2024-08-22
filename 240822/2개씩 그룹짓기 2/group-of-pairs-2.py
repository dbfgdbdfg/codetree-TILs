n=int(input())
a_list=list(map(int,input().split()))
a_list.sort()
#[2, 5, 7, 9, 10, 15]
b_list=[]

for i in range(n):
    b_list.append(abs(a_list[i]-a_list[i+n]))
print(min(b_list))