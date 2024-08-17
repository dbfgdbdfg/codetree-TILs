n=int(input())
a_list=list(map(int,input().split()))
#[2, 1, 6, 2, 7, 8]

sums=0
sum_list=[]
for i in range(n-2):
    for q in range(i+2,n):
        sums=a_list[i]+a_list[q]
        sum_list.append(sums)
        sums=0

print(max(sum_list))