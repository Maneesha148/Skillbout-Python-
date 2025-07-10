class Employee:
    def work(self):
        print("Employee work")
class Manager(Employee):
    def manage(self):
        print("Manager work")
m=Manager()
m.work()
m.manage()
