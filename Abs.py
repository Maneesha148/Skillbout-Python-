from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand
    @abstractmethod
    def start_engine(self):
        pass
    def display_brand(self):
        print(f"Brand: {self.brand}")
class Car(Vehicle):
    def start_engine(self):
        print(f"{self.brand} engine started with a key ignition.")
class ElectricScooter(Vehicle):
    def start_engine(self):
        print(f"{self.brand} engine started silently with a button.")
my_car = Car("Toyota")
my_scooter = ElectricScooter("Ather")
my_car.display_brand()
my_car.start_engine()
my_scooter.display_brand()
my_scooter.start_engine()
