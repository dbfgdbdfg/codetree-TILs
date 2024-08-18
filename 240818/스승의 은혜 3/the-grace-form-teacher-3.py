n,b=map(int,input().split())

class Great:
    def __init__(self, p, s, t):
        self.p = p
        self.s = s
        self.t = t

a_list = []
for i in range(n):
    p, s = map(int, input().split())
    a_list.append(Great(p, s, p+s))

cost=0
student=0
a_list.sort(key=lambda x:x.t)

available_num=[]

for i in range(n):
    if cost + a_list[i].t <= b:
        cost += a_list[i].t
        student += 1
    else:
        break
#print(cost,student)

#선물 받은애들을 b 아닌 애들을 C로

b_list=a_list[:student]
c_list=a_list[student:]
first_student=student
student_list=[]
student_list.append(student)
#쿠폰을 이미 준 애들한테 쓸때
for i in range(student):
    b_list.sort(key=lambda x:x.p)
    discounted_cost=cost-b_list[-1].p//2
    for i in range(n-student):
        if discounted_cost+c_list[i].t<=b:
            discounted_cost+=c_list[i].t
            student+=1
    student_list.append(student)
    student=first_student

#쿠폰을 안준 애들한테 줄때
for i in range(n-student):
    if cost+c_list[i].p//2 + c_list[i].s<=b:
        cost+=c_list[i].p//2 + c_list[i].s
        student+=1
    student_list.append(student)
    student=first_student
print(max(student_list))