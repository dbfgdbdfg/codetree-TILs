n,k=map(int,input().split())
a_list=list(map(int,input().split()))
a_list.sort()
b_list=[]

def Great(first,end,a_list):
    sums=0
    for i in range(len(a_list)):
        if a_list[i]>=first and a_list[i]<=end:
            sums+=0
        elif a_list[i]<first:
            sums+=first-a_list[i]
        elif a_list[i]>end:
            sums+=a_list[i]-end
    #print(a_list)
    return sums
#3 20 27 62 
first=a_list[0]
end=first+k
#print(first,end)
sums=0
sum_list=[]
for i in range(first,a_list[-1]-k+1):
    sum_list.append(Great(i,i+k,a_list))    

print(min(sum_list))