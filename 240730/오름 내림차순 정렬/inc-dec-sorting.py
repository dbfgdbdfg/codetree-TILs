n=int(input())
a_list=list(map(int,input().split()))
a_list.sort()
for i in range(n):
    print(a_list[i],end=" ")
a_list.sort(reverse=True)
print()
for i in range(n):
    print(a_list[i],end=" ")