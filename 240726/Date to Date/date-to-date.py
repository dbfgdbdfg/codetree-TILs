days=[31,28,31,30,31,30,31,31,30,31,30,31]
w=input().split()
a,b,c,d=int(w[0]),int(w[1]),int(w[2]),int(w[3])

date=0
for i in range(a-1,c-1):
    date+=days[i]
date=date + d - b +1
print(date)

#3.2부터 6.5 이면 3월 4월 5월 함하고 2빼고 5더하기