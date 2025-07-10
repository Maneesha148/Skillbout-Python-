class Animal:
    def make_sound(self):
        print("Making sound")
class Dog(Animal):
    def make_sound(self):
        print(" Dog Making sound")
class Cat(Animal):
    def make_sound(self):
        print(" Cat Making sound")
for v in [Dog(),Cat()]:
    v.make_sound()
