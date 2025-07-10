from abc import ABC, abstractmethod
class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass
class Washingmachine(Appliance):
    def turn_on(self):
        return "Washingmachine turned on"
class Fridge(Appliance):
    def turn_on(self):
        return "Fridge turned on"
obj=Fridge()
print(obj.turn_on())