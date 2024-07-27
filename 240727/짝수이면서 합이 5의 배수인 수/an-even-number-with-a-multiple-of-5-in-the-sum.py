n=int(input())

def number(a):
    return a%2==0 and (a//10+a%10)%5==0
if number(n):
    print("Yes")
else:
    print("No")