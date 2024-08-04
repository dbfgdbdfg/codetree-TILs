w=input().split()
n,k=int(w[0]),int(w[1])

a_list=[0]*n

for i in range(k):
    w=input().split()
    a,b=int(w[0]),int(w[1])
    for q in range(a,b+1):
        a_list[q-1]+=1
print(max(a_list))
    
#2칸 4칸 범위 234