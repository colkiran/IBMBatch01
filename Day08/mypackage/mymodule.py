
gname = "Sachin"

sports = ['cricket', 'tennis', 'hockey', 'football', 'swimming']

runs = {'test': 14500, 'odi': 18300, 't20': 2500}

def greet(gnm):
    print(f"Greetings {gnm}, Welcome to the event.....")

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        print(f"Name is {self.name}\nSalary is {self.salary}")

print(__name__)     # name of the module
# __main__ if the mymodule file is executed
# mymodule if consumed in some other file

if __name__ == '__main__':
    greet("Dhoni")
    emp1 = Employee('Jack', 75000)
    emp1.get_details()


