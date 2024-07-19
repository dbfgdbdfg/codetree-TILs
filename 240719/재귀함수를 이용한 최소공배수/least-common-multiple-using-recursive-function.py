n=int(input())
w=input().split()
a_list=[]
for i in range(n):
    a=int(w[i])
    a_list.append(a)

b_list=[]
for i in a_list:
    nums=0
    for q in range(2,i):        
        if i%q==0:
            b_list.append(q)
            nums+=1
        if nums==0:
            b_list.append(i)

b__list=list(set(b_list))

for a in b__list:
    for w in b__list:
        if w!=a and w%a==0:
            b__list.remove(a)
final=1
for i in b__list:
    final*=i
print(final)

'''
b_list=[]
c_list=[]

for i in range(1,10):
    t=nums/i
    final=t
    for q in a_list:        
        c_list.append(t%q)
        c__list=list(set(c_list))
    if c__list==[0.0]:
        b_list.append(final)
print(b_list)       
#print(int(min(b_list)))
'''