class Great:
    def __init__(self,code,line,time):
        self.code=code
        self.line=line
        self.time=time

w=input().split()
a,b,c=w[0],w[1],w[2]

what=Great(a,b,c)

print("code : "+what.code)
print("color : "+what.line)
print("second : "+what.time)