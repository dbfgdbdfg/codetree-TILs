a=str(input())
b=str(input())

a_list=list(a)
b_list=list(b)
if len(a_list)==len(b_list):
    if a_list.sort()==b_list.sort():
        print("Yes")
    else:
        print("No")
else:
    print("No")