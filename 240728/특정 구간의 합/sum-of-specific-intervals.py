w=input().split()
n,m=int(w[0]),int(w[1])
global a_list
a_list=[]
a_list=input().split()


for i in range(m):
    w1=input().split()
    a1,a2=int(w1[0]),int(w1[1])
    sums=0
    for q in range(a1-1,a2):
        sums+=int(a_list[q])
    print(sums)