n=int(input())
a_list=[]
first=0
final=0
for i in range(n):
    w=input().split()
    a,b=int(w[0]),w[1]
    if b=="R":
        for i in range(0,a):
            a_list.append(first+i)
        first+=a
    if b=="L":
        for i in range(0,a):
            a_list.append(first-i)
        first-=a

b_list=set(a_list)
#print(a_list)
#print(b_list)
for i in b_list:
    t=a_list.count(i)
    if t>=2:
        final+=1
    
print(final)