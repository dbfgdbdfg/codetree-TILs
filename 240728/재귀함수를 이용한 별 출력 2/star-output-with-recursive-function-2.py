n=int(input())

for a in range(n,0,-1):
    for i in range(a):
        print("*",end=" ")
    print()
for a in range(1,n+1):
    for i in range(a):
        print("*",end=" ")
    print()