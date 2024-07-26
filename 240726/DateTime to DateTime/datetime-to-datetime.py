w=input().split()
a,b,c=int(w[0]),int(w[1]),int(w[2])
date=0
first=a*24*60+b*60+c
late=11*24*60+11*60+11
if first>=late:
    print(first-late)
else:
    print(-1)