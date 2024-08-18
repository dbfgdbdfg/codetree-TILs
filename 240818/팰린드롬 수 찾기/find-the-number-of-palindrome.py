x,y=map(int,input().split())

a_list=[]
nums=0

def Great(n):
    n=str(n)
    what=len(n)//2
    for i in range(what):
        if n[i]==n[-i-1]:
            return True
        else:
            return False
            break

#짝수면 0이랑 -1 이랑 1이랑 -2이랑 같아야 됨




for i in range(x,y+1):
    if Great(i):
        nums+=1
print(nums)