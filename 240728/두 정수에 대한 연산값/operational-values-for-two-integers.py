w=input().split()

a,b=int(w[0]),int(w[1])

def great(a,b):
    if a>b:
        a+=25
        b*=2
        print(a,b)
    else:
        a*=2
        b+=25
        print(a,b)

great(a,b)