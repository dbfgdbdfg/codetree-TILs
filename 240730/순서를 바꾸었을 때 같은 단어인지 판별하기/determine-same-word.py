a=str(input())
b=str(input())
a_list=list(a)
b_list=list(b)
a_list.sort()
b_list.sort()

if len(a_list)==len(b_list):
    if a_list==b_list:
        print("Yes")
    else:
        print("No")
else:
    print("No")