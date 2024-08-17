n,s=map(int,input().split())
n_list=list(map(int,input().split()))
n_sums=sum(n_list)
#[5, 7, 9, 1, 13, 8]
sums=0
sum_list=[]


for q in range(n-1):
    for w in range(q+1,n):
        sums=n_sums-n_list[q]-n_list[w]
        sum_list.append(abs(s-sums))
        
print(min(sum_list))