class Great:
    def __init__(self,name,high,weig):
        self.name=name
        self.high=high
        self.weig=weig

n=5
a_list=[]
for i in range(n):
    w=input().split()
    a_list.append(Great(w[0],int(w[1]),w[2]))

a_list.sort(key=lambda a:a.name)
print("name")
for Great in a_list:
    print(Great.name,Great.high,Great.weig)
print( )

a_list.sort(key=lambda a:-a.high)
print("height")
for Great in a_list:
    print(Great.name,Great.high,Great.weig)