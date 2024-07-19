n=int(input())
w=input().split()
a_list=[]
b_list=[]
for i in range(1,n+1):
    if i%2==1:
        a_list=w[:i]
 
        b_list = sorted(a_list, key=lambda x: int(x))

        t=i//2+1

        print(b_list[t-1],end=" ")