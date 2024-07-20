w=input().split()
n,m=int(w[0]),int(w[1])

def minin(n,m):
    a_list=[]
    for i in range(1,m+1):
        if m%i==0 and n%i==0:
            a_list.append(i)
    b=max(a_list)
    print(int(n*m/b))
minin(n,m)