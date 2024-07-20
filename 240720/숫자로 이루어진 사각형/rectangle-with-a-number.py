def make_star(n):
    a_list=[1,2,3,4,5,6,7,8,9]
    a=0
    for i in range(n):
        for i in range(n):
            a+=1
            if a>9:
                a-=9
        
            print(a_list[a-1],end=" ")
        print()
make_star(int(input()))