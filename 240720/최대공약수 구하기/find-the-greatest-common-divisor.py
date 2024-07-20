w=input().split()
n,m=int(w[0]),int(w[1])

def maxe(n,m):
    a_list=[]
    for i in range(1,n+1):
        if m%i==0 and n%i==0:
            a_list.append(i)
    print(max(a_list))
maxe(n,m)