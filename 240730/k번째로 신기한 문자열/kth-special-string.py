w=input().split()

a,b,c=int(w[0]),int(w[1]),w[2]
a_list=[]
for i in range(a):
    w=str(input())
    if w[:2]==c:
        a_list.append(w)

a_list.sort()
print(a_list[b-1])