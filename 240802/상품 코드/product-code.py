class Great:
    def __init__(self,name=0,code=0):
        self.name=name
        self.code=code


first=Great()
second=Great()

first.name="codetree"
first.code="50"

w=input().split()
second.name=w[0]
second.code=w[1]

print("product",first.code,"is",first.name)
print("product",second.code,"is",second.name)