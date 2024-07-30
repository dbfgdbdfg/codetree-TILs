w=input().split()

a,b,c=int(w[0]),int(w[1]),w[2]
a_list=[]
for i in range(a):
    e=str(input())
    if e[:len(c)]==c:
        a_list.append(e)

a_list.sort()
print(a_list[b-1])