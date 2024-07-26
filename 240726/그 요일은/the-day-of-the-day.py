w=input().split()
m1,d1,m2,d2=int(w[0]),int(w[1]),int(w[2]),int(w[3])
day =str(input())
a_list=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
day_list=a_list.index(day)

month=[0,31,29,31,30,31,30,31,31,30,31,30,31]

date=0
for i in range(m1,m2):
    date+=month[i]
date=date+d2-d1
#만약 7이면
want=(date-day_list)//7   #0
want_1=date-want*7
if want_1>=day_list:
    want+=1
print(want)