a=str(input())
a_list=[]

def great(n):
    for i in range(len(n)):

        a_list.append(n[i])
    if len(set(a_list))>1:
        return True
if great(a):
    print("Yes")
else:
    print("No")