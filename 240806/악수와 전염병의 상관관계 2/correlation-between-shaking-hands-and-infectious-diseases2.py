n,k,p,t=map(int,input().split())

a_list=[0]*n
k_list=[0]*n
class Great():
    def __init__(self,time,x,y):
        self.time=time
        self.x=x
        self.y=y

programmer=[]
for i in range(t):
    a,b,c=map(int,input().split())
    programmer.append(Great(a,b,c))

programmer.sort(key=lambda a:a.time)
#주어진 것을 시간순으로 배열 정리
#총 T번 한다 그리고 k동안만 옮기고 P가 최초 감염자

a_list[p-1]=1


for i in range(t):
    if a_list[programmer[i].x-1]==1:
        if k_list[programmer[i].x-1]<k:
            a_list[programmer[i].y-1]=1
            k_list[programmer[i].x-1]+=1
    if a_list[programmer[i].y-1]==1:
        if k_list[programmer[i].y-1]<k:
            a_list[programmer[i].x-1]=1
            k_list[programmer[i].y-1]+=1
        
#print(a_list)
#print(k_list)
for i in a_list:
    print(i,end="")
#1234