n,k=map(int,input().split())
a_list=list(map(int,input().split()))
a_list.sort()
max_num=max(a_list)
min_num=min(a_list)
chai=max_num-min_num
'''
b_list=[]
def Great(max_num,min_num,a_list):
    #while sum(a_list)//n >= max_num-min_num//2 :
        max_num-=1
        for i in a_list:
            if min_num<=i<=max_num:
                continue
            else:
                b_list.append(min(abs(i-min_num),abs(i-max_num)))
        print(b_list)
'''

sums=0
if chai<=k:
    print("0")
else:
    if sum(a_list)//n <= max_num-min_num//2:
        while sum(a_list)//n <= max_num-min_num//2:
            max_num-=1
            if max_num-min_num==k:
                #print(max_num,min_num)
                break
    if sum(a_list)//n > max_num-min_num//2:
        while sum(a_list)//n >= max_num-min_num//2:
            min_num-=1
            if max_num-min_num==k:
                #print(max_num,min_num)
                break
   
    for i in a_list:
        if i>max_num:
            sums+=i-max_num
        elif i<min_num:
            sums+=min_num-i
    print(sums)


        #이러면 더 큰쪽에 치우쳐진거니까 큰것부터 내려가자











#그럼 지금 최소 최대 차이 알고 그 차이가 k가 될려면 만야 차이가 10인데 k가 3이면 칸 2칸으로 가면 됨
#차이 - k하고 2로 나누면 될것같은데 이게 2로 안 나누어지면 1 2로 해야되네 그럼 더 큰게 뭔지에 따라 달라지겠네 

#최대와의 차이를 확인하기