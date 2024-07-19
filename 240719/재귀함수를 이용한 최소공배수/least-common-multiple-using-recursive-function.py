n=int(input())
w=input().split()
a_list=[]
nums=1
for i in range(n):
    a=int(w[i])
    a_list.append(a)
    nums*=a
b_list=[]
for i in range(1,max(a_list)):
    t=nums/i
    final=t
    for q in a_list:
        
        if t%q!=0:
            final=0   
    if final!=0:
        b_list.append(final)
        
print(int(min(b_list)))