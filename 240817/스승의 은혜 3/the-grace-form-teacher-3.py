n,b=map(int,input().split())
class Great:
    def __init__ (self,p,s,t): #cost p s 라는 클래스
        self.p=p
        self.s=s
        self.t=t
a_list=[]        
for i in range(n):
    w=input().split()
    a_list.append(Great(int(w[0]),int(w[1]),int(w[0])+int(w[1])))

cost=0
student=0
available_num=[]

while cost<=b:
    for i in range(n):    
        cost+=a_list[i].t
        student+=1
for q in range(n):
    if (cost-a_list[q].p/2)<=b:
        available_num.append(student)
    else:
        available_num.append(student-1)


print(max(available_num))
    



'''
for i in range(n):
    b_list=a_list.copy()
    b_list[i].p=(b_list[i].p)/2
    while cost<=b:
        for q in range(n):  
            cost=b_list[i].p+b_list[i].s
    print(q)
        
'''