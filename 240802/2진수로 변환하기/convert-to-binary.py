n=int(input())

what=[]

while True:
    if n<2:
        what.append(n)
        break
    what.append(n%2)
    n//=2

for i in what[::-1]:
    print(i,end="")