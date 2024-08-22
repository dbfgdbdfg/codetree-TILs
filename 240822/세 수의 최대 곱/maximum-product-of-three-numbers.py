n=int(input())
a_list=list(map(int,input().split()))
a_list.sort()
#[-20, -9, -5, -3, -2, 0, 1, 4, 6, 7, 10, 15]
sum_list=[]

plus_num=0
minus_num=0
zero_num=0
for i in range(n):
    if a_list[i]>0:
        plus_num+=1
    elif a_list[i]<0:
        minus_num+=1
    else:
        zero_num+=1

if minus_num>=2 and plus_num>=1:
    sums=a_list[0]*a_list[1]*a_list[-1]
    sum_list.append(sums)
if plus_num>=3:
    sums=a_list[-1]*a_list[-2]*a_list[-3]
    sum_list.append(sums)
if minus_num<=1:
    for i in range(n):
        a_list[i]=abs(a_list[i])
        a_list.sort()
    sums=-(a_list[0]*a_list[1]*a_list[2])
    sum_list.append(sums)
print(max(sum_list))