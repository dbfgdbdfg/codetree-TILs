n=int(input())
a_list=[]
for i in range(n):
    a=input()
    w=a.split()
    if w[2]=="Rain":
        a_list.append(a)
for i in a_list:
    for q in a_list:
        if int(i[:3])<int(q[:3]):
            print(i)
        if int(i[:3])==int(q[:3]):
            if int(i[5:7])<int(q[5:7]):
                print(i)

            if int(i[5:7])==int(q[5:7]):

                if int(i[8:10])<int(q[8:10]):
                    print(i)