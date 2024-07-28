n=str(input())
m=str(input())

def great(a,b): 
    c=len(b)
    what="-1"
    for i in range(len(a)-len(b)+1):

        if b==a[i:i+len(b)]:

            what=i
            break
    print(what)

    
great(n,m)