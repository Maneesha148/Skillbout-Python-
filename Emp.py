class Emp:
    def __init__(self,name,sal,age):
        self.__name = name
        self.__sal = sal
        self.__age = age
    def set_name(self,name):
        self.__name = name
    def get_name(self):
        return self.__name
    def set_sal(self,sal):
        self.__sal = sal
    def get_sal(self):
        if self.__sal>0:
            return self.__sal
        else:
            return "Salary must be greater than 0."
    def set_age(self,age):
        self.__age = age
    def get_age(self):
        if self.__age<18 or self.__age>100:
            return "Age must be between 18 and 100"
        else:
            return self.__age
name=input("Name: ")
sal=float(input("Salary: "))
age=int(input("Age: "))
obj=Emp(name,sal,age)
print("Employee Name: ",obj.get_name())
print("Employee Salary: ",obj.get_sal())
print("Employee Age: ",obj.get_age())
