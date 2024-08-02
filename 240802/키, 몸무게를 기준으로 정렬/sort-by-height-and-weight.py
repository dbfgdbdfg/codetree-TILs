n=int(input())
a_list=[]
class Great:
    def __init__(self,name,heigh,weight):
        self.name=name
        self.heigh=heigh
        self.weight=weight
for i in range(n):
    w=input().split()
    a_list.append(Great(w[0],int(w[1]),int(w[2])))

a_list.sort(key=lambda a:(a.heigh,-a.weight))

for Great in a_list:
    print(Great.name,Great.heigh,Great.weight)