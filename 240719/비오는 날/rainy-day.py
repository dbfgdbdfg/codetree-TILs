n=int(input())
a_list=[]
for i in range(n):
    a=input()
    w=a.split()
    if w[2]=="Rain":
        a_list.append(a)

#['2037-12-27 Sun Rain', '2036-08-28 Wed Rain', '2043-03-21 Sat Rain', '2077-08-19 Thu Rain']
b_list=[]
for i in a_list:
    ai=i[:4]+i[5:7]+i[8:10]
    b_list.append(int(ai))
what = b_list.index(min(b_list))

    #for q in a_list:

print(a_list[what])