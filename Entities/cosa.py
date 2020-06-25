class vaca:
    def __init__(self,name):
        self.name = name

    def newName(self,name):
        self.name = name

    def __repr__(self):
        return self.name

a = vaca("lola")
dic = {"vaca": a}
print(dic)

v = dic["vaca"]

v.newName("ramona")
print(v)

print(dic)
