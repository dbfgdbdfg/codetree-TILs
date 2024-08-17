a_list=[list(map(int,input().split()))
for i in range(19)]

class Great:
    def __init__ (self,r,c):
        self.r=r
        self.c=c

white=False
white_list=[]
black=False
black_list=[]

for r in range(19):
    for c in range(19):
        if a_list[r][c]==1:
            if r+4<19 and a_list[r+1][c]==1:
                if a_list[r+2][c]==a_list[r+3][c]==a_list[r+4][c]==1:
                    black=True
                    black_list.append(Great(r+2,c))
            if c+4<19 and a_list[r][c+1]==1:
                if a_list[r][c+2]==a_list[r][c+3]==a_list[r][c+4]==1:
                    black=True
                    black_list.append(Great(r,c+2))
            if r+4<19 and c+4<19 and a_list[r+1][c+1]==1:
                if a_list[r+2][c+2]==a_list[r+3][c+3]==a_list[r+4][c+4]==1:
                    black=True
                    black_list.append(Great(r+2,c+2))
            if r-5>0 and c+4<19 and a_list[r-1][c+1]==1:
                if a_list[r-2][c+2]==a_list[r-3][c+3]==a_list[r-4][c+4]==1:
                    black=True
                    black_list.append(Great(r-2,c+2))
        elif a_list[r][c]==2:
            if r+4<19 and a_list[r+1][c]==2:
                if a_list[r+2][c]==a_list[r+3][c]==a_list[r+4][c]==2:
                    white=True
                    white_list.append(Great(r+2,c))
            if c+4<19 and a_list[r][c+1]==2:
                if a_list[r][c+2]==a_list[r][c+3]==a_list[r][c+4]==2:
                    white=True
                    white_list.append(Great(r,c+2))
            if c+4<19 and r+4<19 and a_list[r+1][c+1]==2:
                if a_list[r+2][c+2]==a_list[r+3][c+3]==a_list[r+4][c+4]==2:
                    white=True
                    white_list.append(Great(r+2,c+2))
            if r-4>=0 and c+4<19 and a_list[r-1][c+1]==2:
                if a_list[r-2][c+2]==2 and a_list[r-3][c+3]==2 and a_list[r-4][c+4]==2:
                    white=True
                    white_list.append(Great(r-2,c+2))


if black==True:
    print("1")
    print(black_list[0].r+1,black_list[0].c+1)
elif white==True:
    print("2")
    print(white_list[0].r+1,white_list[0].c+1)
else:
    print("0")