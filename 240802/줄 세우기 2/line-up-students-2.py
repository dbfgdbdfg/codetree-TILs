n=int(input())

class Great:
    def __init__(self,height,weight,inde):
        self.height=height
        self.weight=weight
        self.inde=inde
a_list=[]
for i in range(n):
    w=input().split()
    a_list.append(Great(int(w[0]),int(w[1]),i+1))

a_list.sort(key=lambda a:(a.height, -a.weight))

for Great in a_list:
    print(Great.height,Great.weight,Great.inde)