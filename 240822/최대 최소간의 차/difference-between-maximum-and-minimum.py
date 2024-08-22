n,k=map(int,input().split())
a_list=list(map(int,input().split()))
a_list.sort()
max_num=max(a_list)
min_num=min(a_list)
chai=max_num-min_num

def Great(a_list, max_num, min_num):
    # 차이 유지
    chai = max_num - min_num
    
    while True:
        plus_num = 0
        minus_num = 0
        
        # plus_num과 minus_num 계산
        for i in a_list:
            if i > max_num:
                plus_num += 1
            elif i < min_num:
                minus_num += 1
        
        if plus_num == minus_num:
            return max_num, min_num
        
        # 조정 로직
        if plus_num > minus_num:
            # plus_num이 더 클 때 max_num을 감소
            max_num -= 1
        elif plus_num < minus_num:
            # minus_num이 더 클 때 min_num을 증가
            min_num += 1
        
        # 차이를 유지
        if max_num - min_num != chai:
            max_num += 1
            min_num -=1
        

'''
def Great(a_list,max_num,min_num):
    plus_num=0
    minus_num=0
    for i in a_list:
        if i>max_num:
            plus_num+=1
        if i<min_num:
            minus_num+=1
    if plus_num>minus_num:
        Great(a_list,max_num+1,min_num+1)
    if plus_num<minus_num:
        Great(a_list,max_num-1,min_num-1)
    return max_num,min_num
'''
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
        while sum(a_list)//n > max_num-min_num//2:
            min_num+=1
            if max_num-min_num==k:
                #print(max_num,min_num)
                break
    print(max_num,min_num)
    b_list=[]
    max_num,min_num=Great(a_list,max_num,min_num)
    sums=0
    for i in range(n):
        if a_list[i]>max_num:
            sums+=a_list[i]-max_num
        elif a_list[i]<min_num:
            sums+=min_num-a_list[i]
    print(sums)



#35 32
#[-28, -18, -2, 23, 33]


'''
 for i in range(n):
        if a_list[i]>max_num:
            b_list.append(a_list[i]-max_num)
            plus_num+=1
        elif a_list[i]<min_num:
            b_list.append(a_list[i]-min_num)
            minus_num+=1
for i in range(n):
            if a_list[i]>max_num:
                sums+=a_list[i]-max_num
            elif a_list[i]<min_num:
                sums+=a_list[i]-min_num
        print(sums)
    for i in range(n):
        if a_list[i]>max_num:
            plus_num+=1
        elif a_list[i]<min_num:
            minus_num+=1
def Great(a_list,max_num,min_num ,plus_num=0,minus_num=0):
    for i in range(len(a_list)):
        if a_list[i]>max_num:
            plus_num+=1
        elif a_list[i]<min_num:
            minus_num+=1
    if plus_num>minus_num:
        Great(a_list,max_num+1,min_num+1,plus_num,minus_num)
    if plus_num<minus_num:
        Great(a_list,max_num+1,min_num+1,plus_num,minus_num)
    if plus_num==minus_num:
        return max_num,min_num
'''





#그럼 지금 최소 최대 차이 알고 그 차이가 k가 될려면 만야 차이가 10인데 k가 3이면 칸 2칸으로 가면 됨
#차이 - k하고 2로 나누면 될것같은데 이게 2로 안 나누어지면 1 2로 해야되네 그럼 더 큰게 뭔지에 따라 달라지겠네 

#최대와의 차이를 확인하기