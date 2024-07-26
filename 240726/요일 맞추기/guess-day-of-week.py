days=["Sun","Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
month=[0,31,28,31,30,31,30,31,31,30,31,30,31]
w=input().split()
m1,d1,m2,d2=int(w[0]),int(w[1]),int(w[2]),int(w[3])

date=0
if m1<=m2:
    for i in range(m1,m2):
        date=date+month[i]
    date = date +d2-d1 +7
if m1>m2:
    for i in range(m2,m1):
        date=date-month[i]
    date = date -d1+d2


i=(date%7 + 1)%7

print(days[i])