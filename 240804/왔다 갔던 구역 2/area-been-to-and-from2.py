n = int(input())
a_list = []

first=0

for i in range(n):
    w=input().split()
    a,b=int(w[0]),w[1]
    if b=="R":
        end=first+a
        a_list.append([first,end])
        first+=a
    if b=="L":
        end=first-a
        a_list.append([end,first])
        first-=a
	
b_list = [0] *2000

for x,y in a_list:
    for i in range(x+1000,y+1000):
        b_list[i]+=1


cnt = 0

for elem in b_list:
	if elem >= 2:
		cnt += 1
print(cnt)