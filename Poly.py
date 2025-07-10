class Poly:
    def show(self,a=None,b=None,c=None):
        if a and b and c:
            print(a,b,c)
        elif a and b:
            print(a,b)
        elif a:
            print(a)
        else:
            print("None")
a=Poly()
a.show()
a.show(1,2,3)