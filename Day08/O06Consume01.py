
import mymodule as m
from mymodule import Employee

print(f"Sports :{m.sports}")

print(f"Runs :{m.runs}")

print("-" * 60)
m.greet("PV Sindhu")

print("-" * 60)
emp1 = Employee("John", 45000)
emp1.get_details()
