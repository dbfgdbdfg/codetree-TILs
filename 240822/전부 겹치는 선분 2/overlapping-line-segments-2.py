n=int(input())
class Great:
    def __init__ (self,x,y):
        self.x=x
        self.y=y
a_list=[]
for i in range(n):
    w=input().split()
    a_list.append(Great(w[0],w[1]))
b_list=[]
what_list=[]
for i in range(n):
    b_list=a_list.copy()
    del b_list[i]
    what=True
    for q in range(n-2):
        for w in range(q+1,n-1):
            if b_list[q].y<b_list[w].x or b_list[w].y<b_list[q].x:
                what=False
    what_list.append(what)
    if what==True:
            print("Yes")
            break
if True not in what_list:
    print("No")