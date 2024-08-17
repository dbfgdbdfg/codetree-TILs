a_list=list(map(int,input().split()))
a_list.sort()
solo=max(a_list)
del a_list[4]
total_sums=sum(a_list)

class Great:
    def __init__ (self,x,y,z=solo):
        self.x=x
        self.y=y
        self.z=z

possible=True

def what(x,y,z):
    if x==y or y==z or x==z:
        possible = False
    else:
        total_list.append((max(x,y,z)-min(x,y,z)))

sum_list=[]
total_list=[]

for i in range(3):
    for q in range(i+1,4):
        sum_list.append(Great(a_list[i]+a_list[q],total_sums-a_list[i]-a_list[q]))

for i in range(len(sum_list)):
    what(sum_list[i].x,sum_list[i].y,sum_list[i].z)
    #print(sum_list[i].x,sum_list[i].y,sum_list[i].z)
if possible==True:
    print(min(total_list))
else:
    print("-1")