class Great:
    def __init__(self,name=0,num=0,place=0):
        self.name=name
        self.num=num
        self.place=place

n=int(input())
a_list=[]
for i in range(n):
    w=input().split()
    a_list.append(Great(w[0],w[1],w[2]))

new_list=sorted(a_list,key=lambda obj:obj.name)

print("name",new_list[n-1].name)
print("addr",new_list[n-1].num)
print("city",new_list[n-1].place)