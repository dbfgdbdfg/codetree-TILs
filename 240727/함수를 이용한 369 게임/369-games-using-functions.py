def inside(n):
    n1=str(n)
    return ("3" in n1) or ("6" in n1) or ("9" in n1)
    

def basu(n):
    return n%3==0 or inside(n)


cnt=0

w=input().split()
a,b=int(w[0]),int(w[1])
for i in range(a,b+1):
    if basu(i):
  
        cnt+=1
print(cnt)