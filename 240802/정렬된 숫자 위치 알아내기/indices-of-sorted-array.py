n=int(input())
a_list=[]
class Great:
    def __init__(self,what,first,inde=0):
        self.what=what
        self.first=first
        self.inde=inde

w=input().split()

for i in range(n):
    a_list.append(Great(int(w[i]),i+1))

a_list.sort(key=lambda a:a.what)

for i in range(n):
    a_list[i].inde=i+1

a_list.sort(key=lambda a:a.first)

for Great in a_list:
    print(Great.inde,end=" ")