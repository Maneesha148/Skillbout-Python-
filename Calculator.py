class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def addition(self):
        """Addition of two numbers"""
        res=self.a+self.b
        print(f"Addition({self.a}+{self.b}):{res}")
    def subtraction(self):
        #Subtraction of two numbers
        res=self.a-self.b
        print(f"Subtraction({self.a}-{self.b}):{res}")
    def multiplication(self):
        #Multiplication of two numbers
        res=self.a*self.b
        print(f"Multiplication({self.a}*{self.b}):{res}")
    def division(self):
        #division of two numbers
        try:
            res=self.a/self.b
            print(f"Division({self.a}/{self.b}):{res}")
        except ZeroDivisionError:
            print(f"Division({self.a}/{self.b}): Error.Division by zero is not allowed")
a=10
b=0
obj=Calculator(a,b)
obj.addition()
obj.subtraction()
obj.multiplication()
obj.division()
