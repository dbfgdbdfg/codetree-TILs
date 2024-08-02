n=int(input())

class Great:
    def __init__ (self,name,f,s,t):
        self.f=f
        self.s=s
        self.t=t
        self.name=name
a_list=[]
for i in range(n):
    w=input().split()
    a_list.append(Great(w[0],int(w[1]),int(w[2]),int(w[3])))

a_list.sort(key=lambda a: a.f+a.s+a.t)

for Great in a_list:
    print(Great.name,Great.f,Great.s,Great.t)