n=int(input())
#www bbb fff
first=1000
a_list=[0]*2000
w_list=[]
b_list=[]


for i in range(n):
    w=input().split()
    a,b=int(w[0]),w[1]
    if b=="R":
        for t in range(a):
            a_list[first+t]="W"
            w_list.append(first+t)
        first=first+a-1

    if b=="L":
        for t in range(a):
            a_list[first-t]="B"
            b_list.append(first-t)
        first=first-a+1 

#print(w_list,b_list)
for i in w_list:
    if w_list.count(i)>=2 and b_list.count(i)>=2:
        a_list[i]="F"

print(a_list.count("B"),a_list.count("W"),a_list.count("F"))