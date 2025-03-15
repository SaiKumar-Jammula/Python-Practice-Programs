class person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=person("sai",33)
print(p1.name)
print(p1.age)

import math
class sqroot():
    def calc(x):
        r=math.sqrt(x)
        return r
n=int(input())
sq=sqroot.calc(n)
print(sq)
