a_list=list(map(int,input().split()))


total_sums=sum(a_list)

class Great:
    def __init__ (self,x,y,z):
        self.x=x
        self.y=y
        self.z=z


def what(x,y,z):
    if x!=y and y!=z and x!=z:
        total_list.append((max(x,y,z)-min(x,y,z)))

sum_list=[]
total_list=[]

for i in range(5):
    for q in range(5):
        for w in range(5):
            if i!=q and q!=w and w!=i:
                sum_list.append(Great(total_sums-a_list[i]-a_list[q]-a_list[w],a_list[i]+a_list[q],a_list[w]))


for i in range(len(sum_list)):
    what(sum_list[i].x,sum_list[i].y,sum_list[i].z)
    #print(sum_list[i].x,sum_list[i].y,sum_list[i].z)

if len(total_list)>0:
    print(min(total_list))
else:
    print("-1")