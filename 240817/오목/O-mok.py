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

for r in range(14):
    for c in range(14):
        if a_list[r][c]==1:
            if a_list[r+1][c]==1:
                if a_list[r+2][c]==a_list[r+3][c]==a_list[r+4][c]==1:
                    black=True
                    black_list.append(Great(r+2,c))
            if a_list[r][c+1]==1:
                if a_list[r][c+2]==a_list[r][c+3]==a_list[r][c+4]==1:
                    black=True
                    black_list.append(Great(r,c+2))
            if a_list[r+1][c+1]==1:
                if a_list[r+2][c+2]==a_list[r+3][c+3]==a_list[r+4][c+4]==1:
                    black=True
                    black_list.append(Great(r+2,c+2))
        if a_list[r][c]==2:
            if a_list[r+1][c]==2:
                if a_list[r+2][c]==a_list[r+3][c]==a_list[r+4][c]==2:
                    white=True
                    white_list.append(Great(r+2,c))
            if a_list[r][c+1]==2:
                if a_list[r][c+2]==a_list[r][c+3]==a_list[r][c+4]==2:
                    White=True
                    white_list.append(Great(r,c+2))
            if a_list[r+1][c+1]==2:
                if a_list[r+2][c+2]==a_list[r+3][c+3]==a_list[r+4][c+4]==2:
                    White=True
                    white_list.append(Great(r+2,c+2))



if black==True:
    print("1")
    print(black_list[0].r+1,black_list[0].c+1)
elif white==True:
    print("2")
    print(White_list[0].r+1,White_list[0].c+1)
else:
    print("0")