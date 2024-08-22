n=int(input())
class Great():
    def __init__ (self,x,y):
        self.x=x
        self.y=y
a_list=[]
for i in range(n):
    w=input().split()
    a_list.append(Great(int(w[0]),int(w[1])))
line_list=[]
start=0
end=0
for i in range(n):
    b_list=a_list.copy()
    del b_list[i]
    b_list.sort(key=lambda x:x.x)
    start=b_list[0].x
    b_list.sort(key=lambda x:x.y)
    end=b_list[-1].y
    line_list.append(abs(end-start))
print(min(line_list))