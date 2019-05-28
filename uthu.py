class student:
    def __init__(self, name, major):
        self.name = name
        self.age = major

    def myfunc(self):
        print("hello my name is" + self.name)

p1 = student("Dante", "Computer Science")
p2 = student("Charletha", "Computer Science")

print(p1.name)
print(p1.major)

p1.myfunc()

pl.major = "Computer Science"

print(p1.major)

del p1.major

#print(pl.major)
print(p2.major)

del p1
