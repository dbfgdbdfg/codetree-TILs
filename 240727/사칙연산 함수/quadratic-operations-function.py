def plus(a,b):
    return a+b
def minus(a,b):
    return a-b
def mult(a,b):
    return a*b
def squa(a,b):
    return a//b
w1=input()
w=w1.split()

a,b=int(w[0]),int(w[2])

if w[1]=="*":
    print(w1,"=",mult(a,b))
elif w[1]=="+":
    print(w1,"=",plus(a,b))
elif w[1]=="-":
    print(w1,"=",minuss(a,b))
elif w[1]=="/":
    print(w1,"=",squa(a,b))
else:
    print("False")