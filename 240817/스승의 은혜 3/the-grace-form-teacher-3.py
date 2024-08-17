n,b=map(int,input().split())
class Great:
    def __init__ (self,p,s,t): #cost p s 라는 클래스
        self.p=p
        self.s=s
        self.t=t
a_list=[]        
for i in range(n):
    w=input().split()
    #print(int(w[0]),int(w[1]),int(w[0])+int(w[1]))
    a_list.append(Great(int(w[0]),int(w[1]),int(w[0])+int(w[1])))

cost=0
student=0
a_list.sort(key=lambda Great:Great.t)

available_num=[]

for i in range(n):  
    cost+=a_list[i].t
    student+=1
    if cost>=b:
        #print(cost,student)
        break

for q in range(student):
    #print(cost-a_list[q].p//2)
    if (cost-a_list[q].p//2)<=b:
        available_num.append(student)
    else:
        available_num.append(student-1)




b_list=a_list[student:]

b_list.sort(key=lambda Great:Great.s)

for q in range(n-student):
    what=cost-a_list[student-1].t
    if (what+b_list[q].s+b_list[q].p//2)<=b:
        student+=1
        available_num.append(student)




#print(available_num)
print(max(available_num))