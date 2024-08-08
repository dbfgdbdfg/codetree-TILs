n,t=map(int,input().split())
a_list=[[0]*n for i in range(n)]
w=input().split()
r,c,d=int(w[0]),int(w[1]),w[2]
time=0

def move(r,c,n):
    if n=="R":
        c+=1
    if n=="L":
        c-=1
    if n=="U":
        r-=1
    if n=="D":
        r+=1
    return r,c

         
while True:
    time+=1
    if r>=n and d=="D":
        time+=1
        d="U"
    elif c>=n and d=="R":
        time+=1
        d="L"
    elif c<=1 and d=="L":
        time+=1
        d="R" 
    elif r<=1 and d=="U":
        time+=1
        d="D"
    if time>t:
        break
    r,c=move(r,c,d)
    #print(r,c)


print(r,c)