n=int(input())

class Great:
    def __init__(self,name,kor,eng,mat):
        self.name=name
        self.kor=kor
        self.eng=eng
        self.mat=mat
a_list=[]
for i in range(n):
    w=input().split()
    a_list.append(Great(w[0],w[1],w[2],w[3]))

a_list.sort(key=lambda a:(a.kor,a.eng,a.mat) )

for i in range(n-1,-1,-1):
    print(a_list[i].name,a_list[i].kor,a_list[i].eng,a_list[i].mat)