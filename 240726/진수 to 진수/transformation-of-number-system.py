w=input().split()

a,b=int(w[0]),int(w[1])
n=int(input())

lens=len(str(n)) #11이 경우 두글자  

ten_0=0
ten_0=ten_0+n%10
for i in range(lens-1,0,-1):
    ten_0+=(n//(10**i))*8**i
ten=ten_0 #10진수로는 얼마인지
nums=0
while ten_0>=b:
    ten_0=ten_0//b
    nums+=1
#print(nums)
for i in range(nums,-1,-1):
    what=ten//b**i
    ten=ten%b**i
    print(what,end="")