n=int(input())


def great(n):
    if n==1:
        return 1
    if n==2:
        return 2
    

    return great(n-1)+great(n//3)



print(great(n))