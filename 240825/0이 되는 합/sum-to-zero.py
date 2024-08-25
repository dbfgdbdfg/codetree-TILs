n=int(input())
a_list=list(map(int,input().split()))
what=0

for i in range(n-2):
    for q in range(i+1,n-1):
        for w in range(q+1,n):
            if a_list[i]+a_list[q]+a_list[w]==0:
                what+=1

print(what)