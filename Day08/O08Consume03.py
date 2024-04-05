
import sys

# print(sys.path)

sys.path.append("C:\\Delhi")
for pth in sys.path:
    print(pth)

import gurgaon.mymodule as m
from gurgaon.mymodule import Employee, greet

print(m.runs)

print("-" * 60)

emp1 = Employee("John", 60000)
emp1.get_details()
