n,m=map(int,input().split())
class Great:
    def __init__ (self,index,number):
        self.index=index
        self.number=number
w=input().split()
a_list=[]
for i in range(n):
    a_list.append(Great(i+1,int(w[i])))
#a_list index는 위치 number는 거기에 있는 숫자
#시작위치를 1이라고 하면 인덱스의 1이랑 에 해당하는 넘버 확인한뒤에 그 넘버랑 같은 인데그를 확인하면 된
movement=0
move_total=0

def what(i,a_list):
    global movement
    global move_total
    if movement>=m:
        return move_total
    move_total+=a_list[i-1].number
    movement+=1
    what(a_list[i-1].number,a_list)



move_list=[]

for i in range(1,n+1):
    what(i,a_list)
    move_list.append(what(i,a_list))
    movement=0
    move_total=0

print(max(move_list))
    
    
    
    
 

    
'''
def what(i,a_list):
    global movement
    global move_total
    if movement>=m:
        return move_total
    move_total+=a_list[i-1].number
    movement+=1

    what(a_list[i-1].number,a_list)

what(1,a_list)
print(what(1,a_list)'''