n=int(input())
class Great:
    def __init__ (self,x,y):
        self.x=x
        self.y=y
a_list=[]
for i in range(n):
    w=input().split()
    a_list.append(Great(int(w[0]),int(w[1])))
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
    if what == True:
        #print(max(b_list[0].x,b_list[1].x))
        for i in range(int(max(b_list[0].x,b_list[1].x)),min(b_list[0].y,b_list[1].y)+1):
            for w in range(2,n-1):
                if b_list[w].x>i or b_list[w].y<i:
                    what=False

                
    #print(i,what)
    what_list.append(what)


if True not in what_list:
    print("No")
else:
    print("Yes")