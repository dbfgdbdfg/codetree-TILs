w=input().split()
n1,n2=int(w[0]),int(w[1])

a_list=list(map(int,input().split()))
b_list=list(map(int,input().split()))

def right(a,b):
    return all(elem in a for elem in b)
if right(a_list,b_list):
    print("Yes")
else:
    print("No")