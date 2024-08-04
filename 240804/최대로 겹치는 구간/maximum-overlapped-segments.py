n=int(input())

a_list=[0]*201

for i in range(n):
    w=input().split()
    a,b=int(w[0]),int(w[1])
    for q in range(a,b):
        a_list[q+100]+=1
print(max(a_list))

#-100 0 100