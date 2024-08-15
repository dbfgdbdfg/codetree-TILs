r,c=map(int,input().split())

class Great():
    def __init__ (self,r,c):
        self.r=r
        self.c=c


a_list=[list(map(str,input().split()))
for i in range(r)]

w_list=[]
b_list=[]

if a_list[0][0]=="W":
    for x in range(1,r-1):
        for y in range(1,c-1):
            if a_list[x][y]=="B":
                b_list.append(Great(x,y))
    for i in range(len(b_list)):
        for x in range(b_list[i].r+1,r-1):
            for y in range(b_list[i].c+1,c-1):
                if a_list[x][y]=="W":
                    w_list.append(Great(x,y))
        
    print(len(w_list))

# W B W B


if a_list[0][0]=="B":
    for x in range(r):
        for y in range(c):
            if a_list[x][y]=="W":
                w_list.append(Great(x,y))
    for i in range(len(w_list)):
        for x in range(w_list[i].r+1,r-1):
            for y in range(w_list[i].c+1,c-1):
                if a_list[x][y]=="B":
                    b_list.append(Great(x,y))

    print(len(b_list))