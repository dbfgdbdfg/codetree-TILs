#print(ord("A")) ==65 chr(65)==A
n=int(input())
a_list=[]
b_list=[]
for i in range(n):
    a_list.append(i+1)
w=input().split()
for i in range(n):
    b_list.append(ord(w[i])-64)
#print(a_list)#[1, 2, 3, 4]
#print(b_list)#[1, 4, 2 ,3]
def Great(a_list,inse):
    a_list.remove(inse)
    a_list.insert(inse-1,inse)
    return a_list
movement=0

for i in range(n):
    if a_list[i]!=b_list[i]:
        #print(i,"1111")
        what=b_list.index(i+1)
        #print(what,"222")
        movement+=(what-i)
        Great(b_list,i+1)
print(movement)