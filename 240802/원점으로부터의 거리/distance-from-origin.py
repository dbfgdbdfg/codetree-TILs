n=int(input())

class Great:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        
a_list=[]

for i in range(1,n+1):
    w=input().split()
    if int(w[0])<0:
        w[0]=-int(w[0])
    if int(w[1])<0:
        w[1]=-int(w[1])
    a_list.append(Great(int(w[0]),int(w[1]),i))

a_list.sort(key=lambda a:a.x+a.y)

for Great in a_list:
    print(Great.z)