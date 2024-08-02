n=int(input())

class Great:
    def __init__(self,key,wei,num):
        self.key=key
        self.wei=wei
        self.num=num
a_list=[]
for i in range(1,n+1):
    w=input().split()
    a_list.append(Great(int(w[0]),int(w[1]),i))

a_list.sort(key=lambda a:(-a.key,-a.wei,a.num))

for Great in a_list:
    print(Great.key,Great.wei,Great.num)