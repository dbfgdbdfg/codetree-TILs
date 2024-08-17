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

max_students = student

# 쿠폰을 사용해 최대로 선물할 수 있는 학생 수 계산
for i in range(student):
    # i번째 학생에게 쿠폰 사용 시 비용 계산
    discounted_cost = cost - a_list[i].t + (a_list[i].p // 2 + a_list[i].s)
    if discounted_cost <= b:
        max_students = max(max_students, student)

# 쿠폰을 아직 선물하지 않은 학생 중에 사용할 경우를 계산
for i in range(student, n):
    # i번째 학생에게 쿠폰 사용 시 비용 계산
    new_cost = cost + (a_list[i].p // 2 + a_list[i].s) - a_list[student - 1].t
    if new_cost <= b:
        max_students = max(max_students, student + 1)

print(max_students)

'''
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
    if (what+b_list[q].s+b_list[q].p//2)<b:
        student+=1
        available_num.append(student)


#print(available_num)
print(max(available_num))
 '''