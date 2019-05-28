class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("hello my name is" + self.name)

p1 = person("John", 36)
p2 = person("sarah", 30)

print(p1.name)
print(p1.age)

p1.myfunc()

p1.age = 40

print(p1.age)

del p1.age

#print(pl.age)
print(p2.age)

del p1
