n=input()
nums=0

for i in range(len(n)):
    nums=nums*2+int(n[i])

what=nums*17

a_list=[]

while True:
    if what<2:
        a_list.append(what)
        break

    a_list.append(what%2)
    what//=2

for i in a_list[::-1]:
    print(i,end="")