a_list=list(map(int,input()))
b_list=[]

num_list=[]
num=0
for i in range(len(a_list)):
    b_list=a_list.copy()

    b_list[i]=(b_list[i]+1)%2
    for i in range(len(a_list)):
        num=num*2 + b_list[i]
    num_list.append(num)
    num=0 




print(max(num_list))