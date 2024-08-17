n=int(input())
a_list=[]
b_list=[]
for i in range(n):
    a_list.append(int(input()))
#[4, 7, 8, 6, 4]
sums=sum(a_list)
length=0
len_list=[]
for i in range(n):
    b_list=[0]*n
    for q in range(n):
        if q>=i:
            b_list[q]=q-i
        else:
            b_list[q]=q-i+n
    #print(b_list)
    for i in range(n):
        length+=a_list[i]*b_list[i]
    len_list.append(length)
    length=0

    
print(min(len_list))