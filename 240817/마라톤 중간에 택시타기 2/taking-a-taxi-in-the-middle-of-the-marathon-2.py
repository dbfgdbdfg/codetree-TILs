n=int(input())
point_list=[]
class Great():
    def __init__ (self,x,y):
        self.x=x
        self.y=y
for i in range(n):    
    x,y=map(int,input().split())
    point_list.append(Great(x,y))

length=0
len_list=[]

for i in range(1,n-1):
    point_list_copy=point_list.copy()
    del point_list_copy[i]
    for i in range(n-2):
        length=length + abs(point_list_copy[i].x-point_list_copy[i+1].x)+ abs(point_list_copy[i].y-point_list_copy[i+1].y) 
    len_list.append(length)
    length=0
print(min(len_list))