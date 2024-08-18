'''
다 평균으로 만들면 다 5로 만들면
1 2 2 2 0 이니까
애는 64645
전체에서 4배면 3
그럼 일단 다 해서 평균구하기 만약 더 크면
분산이용하나 -1 +2 -2 +2 0 이게 최소가 되도록 정한다음 K가 홀구면 +합이 더 큰쪽으로 2칸 1칸으로

'''
n,k=map(int,input().split())
a_list=list(map(int,input().split()))
#[6, 3, 7, 3, 5]   #print(a_list)
average=round(sum(a_list)/n) #평균 반올림한거 기준이 될것이다
b_list=[]
for i in range(n):
    b_list.append(a_list[i]-average) 
#[1, -2, 2, -2, 0]   #print(b_list)

if k%2==0:
    k_chai=k//2
    for i in range(n):
        if (-k_chai)<=b_list[i] and b_list[i]<=k_chai:
            b_list[i]=0
        if b_list[i]>k_chai:
            b_list[i]=abs(b_list[i]-k_chai)
        if b_list[i]<(-k_chai):
            b_list[i]=abs(b_list[i]+k_chai)
    print(sum(b_list))
minus_sum=0
plus_sum=0

if k%2!=0:
    k_chai=k//2
    for i in range(n):
        if b_list[i]>0:
            plus_sum+=abs(b_list[i])
        if b_list[i]<0:
            minus_sum+=abs(b_list[i])
    if plus_sum>=minus_sum:
        for i in range(n):
            if (-k_chai)<=b_list[i] and b_list[i]<=k_chai+1:
                b_list[i]=0
            if b_list[i]>k_chai+1:
                b_list[i]=abs(b_list[i]-k_chai-1)
            if b_list[i]<(-k_chai):
                b_list[i]=abs(b_list[i]+k_chai)
        print(sum(b_list))
    else:
        for i in range(n):
            if (-k_chai-1)<=b_list[i] and b_list[i]<=k_chai:
                b_list[i]=0
            if b_list[i]>k_chai:
                b_list[i]=abs(b_list[i]-k_chai)
            if b_list[i]<(-k_chai-1):
                b_list[i]=abs(b_list[i]+k_chai+1)
    
    print(sum(b_list))