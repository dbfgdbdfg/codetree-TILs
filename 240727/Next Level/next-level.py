class Code:
    def __init__(self,ide=0,level=0):
        self.ide=ide
        self.level=level
w=input().split()
final=Code(w[0],w[1])
second=Code()

second.ide="codetree"
second.level=10


print("user {0} lv {1}".format(second.ide,second.level))
print("user {0} lv {1}".format(final.ide,final.level))