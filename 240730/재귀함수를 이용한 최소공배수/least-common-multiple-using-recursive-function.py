n=int(input())
w=input().split()
a_list=[]
for i in range(n):
    a=int(w[i])
    a_list.append(a)

b_list=[]
for i in a_list:
    nums=0
    if i==2 or i==3 or i==5 or i==7:
        b_list.append(i)
    if i==6:
        b_list.append(2)
        b_list.append(3)
    if i==4 or i==8 or i==9:
        b_list.append(i)
    if i==10:
        b_list.append(2)
        b_list.append(5)
b__list=list(set(b_list))

for a in b__list:
    if a==3 and (9 in b__list or 6 in b__list):
        b__list.remove(3)
    elif a==4 and (8 in b__list):
        b__list.remove(4)
for a in b__list:
    if a==2 and (4 in b__list or 6 in b__list or 8 in b__list):
        b__list.remove(2)


final=1    
for i in b__list:
    final*=i
print(final)