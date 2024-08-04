w=input().split()

n,b=int(w[0]),int(w[1])
a_list=[]
while True:
    if n<b:
        a_list.append(n)
        break
    a_list.append(n%b)
    n//=b
    
for i in a_list[::-1]:
    print(i,end="")