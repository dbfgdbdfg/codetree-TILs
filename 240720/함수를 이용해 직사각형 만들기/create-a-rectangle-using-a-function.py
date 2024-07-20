w=input().split()
n,m=int(w[0]),int(w[1])

def make_star(n,m):
    for i in range(n):
        print("1"*m)
make_star(n,m)