
import mypackage.mymodule as m
from mypackage.mymodule import Employee, greet

greet("Virat")

print("-" * 60)
emp1 = Employee("Diana", 48000)
emp1.get_details()

print("-" * 60)
print(m.sports)