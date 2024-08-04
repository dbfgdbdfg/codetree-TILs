n=int(input())
#www bbb fff
first=10000
a_list=[0]*20000
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


print(a_list.count("B"),a_list.count("W"))