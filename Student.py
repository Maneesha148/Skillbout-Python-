from uaclient.clouds.azure import AZURE_PRO_LICENSE_TYPE


class Student:
    def __init__(self,name,marks):
        self.__name = name
        self.__marks = marks
    def set_name(self,name):
        #a string representing the student's name
        self.name = name
    def get_name(self):
        #returns the student's name.
        print("Student Name: ",self.name)
    def set_marks(self,marks):
        #an integer representing the student's marks, ranging from 0 to 100
        self.marks = marks
    def get_marks(self):
        #Marks should be between 0 and 100 (both inclusive)
        if self.marks>0 and self.marks<100:
            print("Student Marks: ",self.marks)
        else:
            #print an error message.
            print("Error:Marks should be between 0 and 100")
            print("Student Marks(after invalid input): ",self.__marks)
name="Alice"
marks=85
s=Student(name,marks)
s.set_name("Bob")
s.get_name()
s.set_marks(67)
s.get_marks()

