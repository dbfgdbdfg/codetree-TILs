n=int(input())
a_list=[list(map(int,input().split()))
for i in range(n)]
fi_sum=0
se_sum=0
total_sum_list=[]

for r in range(n):
    for c in range(n-2):
        fi_sum=int(a_list[r][c])+ int(a_list[r][c+1])+int(a_list[r][c+2])
        for q in range(n):
            for w in range(n-2):
                if r!=q:
                    se_sum=a_list[q][w]+a_list[q][w+1] + a_list[q][w+2]
                elif c+2<w or w+2<c:
                    se_sum=a_list[q][w]+a_list[q][w+1] + a_list[q][w+2]
                total_sum_list.append(fi_sum+se_sum)

print(max(total_sum_list))