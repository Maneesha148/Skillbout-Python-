from abc import ABC, abstractmethod
class Dog(ABC):
    @abstractmethod
    def make_sound(self):
        pass
class Cat(Dog):
    def make_sound(self):
        print(" Cat Making sound")
obj=Cat()
obj.make_sound()
"""obj=Dog()
obj.make_sound()"""
