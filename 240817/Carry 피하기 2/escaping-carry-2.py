n=int(input())
a_list=[]
for i in range(n):
    a_list.append(int(input()))
what_list=[]


def Great(x,y,z):
    while max(x,y,z)>10:
        if x%10 + y%10 + z%10 >=10:
            return False
            break
        else:
            x=x//10 
            y=y//10
            z=z//10
            return Great(x,y,z)
    return True
for i in range(n-2):
    for q in range(i+1,n-1):
        for w in range(q+1,n):
            

            if Great(a_list[i],a_list[q],a_list[w])==True:
                sums=a_list[i]+a_list[q]+a_list[w]
                what_list.append(sums)
                sums=0

if len(what_list)>0:
    print(max(what_list))
else:
    print("-1")