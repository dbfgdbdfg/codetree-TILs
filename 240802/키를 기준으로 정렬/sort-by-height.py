n=int(input())

class Great():
    def __init__(self,name,high,wei):
        self.name=name
        self.high=high
        self.wei=wei
a_list=[]
for i in range(n):
    w=input().split()
    a_list.append(Great(w[0],w[1],w[2]))


a_list.sort(key=lambda a :a.high)

for i in range(n):
    print(a_list[i].name,a_list[i].high,a_list[i].wei)
print()