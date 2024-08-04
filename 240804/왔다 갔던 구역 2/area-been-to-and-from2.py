n=int(input())
a_list=[]
first=0
for i in range(n):
    w=input().split()
    a,b=int(w[0]),w[1]
    if b=="R":
        for i in range(1,a+1):
            a_list.append(first+i)
        first+=a
    if b=="L":
        for i in range(1,a+1):
            a_list.append(first-i)
        first-=a

b_list=set(a_list)
print(len(a_list)-len(b_list))