w=input().split()

n,k=int(w[0]),int(w[1])

a_list=list(map(int,input().split()))

a_list.sort()

print(a_list[k-1])