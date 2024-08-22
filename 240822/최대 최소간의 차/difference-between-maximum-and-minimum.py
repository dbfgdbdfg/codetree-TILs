n,k=map(int,input().split())
a_list=list(map(int,input().split()))
a_list.sort()
a_list_sum=sum(a_list)
#print(a_list) #[3, 3, 5, 6, 7]
first_gi=a_list[n//2]
#print(first_gi) #5
for i in range(n):
    a_list[i]=a_list[i]-first_gi
#print(a_list) #[-2, -2, 0, 1, 2]

sums=0

if k%2==0:
    for i in range(n):
        if a_list[i]<=k//2 and a_list[i]>=-k//2:
            a_list[i]=0
        elif a_list[i]>k//2:
            a_list[i]=a_list[i]-k//2
        elif a_list[i]<-k//2:
            a_list[i]=a_list[i]+k//2
    for i in range(n):
        sums+=abs(a_list[i])
    print(sums)
        
if k%2!=0:
    if a_list_sum//n >= first_gi:
        for i in range(n):
            if a_list[i]<=k//2+1 and a_list[i]>=-k//2:
                a_list[i]=0
            elif a_list[i]>k//2+1:
                a_list[i]=a_list[i]-k//2-1
            elif a_list[i]<-k//2:
                a_list[i]=a_list[i]+k//2
    if a_list_sum//n < first_gi:
        for i in range(n):
            if a_list[i]<=k//2 and a_list[i]>=-k//2-1:
                a_list[i]=0
            elif a_list[i]>k//2:
                a_list[i]=a_list[i]-k//2
            elif a_list[i]<-k//2-1:
                a_list[i]=a_list[i]+k//2+1
    
    for i in range(n):
        sums+=abs(a_list[i])
    print(sums)