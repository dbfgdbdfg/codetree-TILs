n,m=map(int,input().split())
class Great:
    def __init__ (self,index,number):
        self.index=index
        self.number=number
w=input().split()
a_list=[]
for i in range(n):
    a_list.append(Great(i+1,int(w[i])))

movement=0
move_total=0

def what(i,a_list,movement=0,move_total=0):

    if movement>=m:
        return move_total
    move_total+=a_list[i-1].number
    movement+=1
    return what(a_list[i-1].number,a_list,movement,move_total)
move_list=[]

for i in range(1,n+1):
    move_list.append(what(i,a_list))


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