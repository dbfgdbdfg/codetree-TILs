'''
아니면 12321이면 최소 거리가 9 그럼
9보다 작으면 최대 속도가 2이어야 되는거지
121 -4
12321-9  -5
1234321-16  -7
123454321-25  -9
'''
n=int(input())
maxver=0
for i in range(n//2+1):
    if i**2<=n and n<=(i+1)**2:
        maxver=i
#최대속도 나왔다 그럼 최대속도가 2인 4부터 8까지의 것드은 일단 n에서 4빼고 
#print(maxver,"h")
extra=n-maxver**2
second=(maxver)*2-1
if maxver==0:
    second=1
#print(extra,second)
if extra<=maxver:
    second+=1
elif extra<=maxver*2:
    second+=2
print(second)