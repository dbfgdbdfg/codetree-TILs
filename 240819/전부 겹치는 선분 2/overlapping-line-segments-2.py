n=int(input())
a_list=[]

class Great:
    def __init__ (self,x,y):
        self.x=x
        self.y=y

for i in range(n):
    w=input().split()
    a_list.append(Great(w[0],w[1]))


b_list=[]
for i in range(n):
    final=True
    b_list=a_list.copy()
    del b_list[i]
    for q in range(n-1):
        for w in range(n-1):
            if q!=w:
                if b_list[q].x>b_list[w].y or b_list[w].x>b_list[q].y:
                    final= False
                #print(i,q,w,final)
    if final==True:
        print("Yes")
        break
if final==False:
    print("No")