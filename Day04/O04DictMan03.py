
print("items".center(60, "-"))
# items is a combination of keys and values functions

emp = {
    'emp1': {'name': 'David', 'age': 34, 'desig': 'MGR', 'dept': 'HR', 'gender': 'male', 'salary': 85000},
    'emp2': {'name': 'Lisa', 'age': 30, 'desig': 'TL', 'dept': 'FIN', 'gender': 'female', 'salary': 60000},
    'emp3': {'name': 'Bernard', 'age': 28, 'desig': 'SE', 'dept': 'IT', 'gender': 'male', 'salary': 115000}
}

print(f"emp :{emp}")
print("-" * 60)

print(f"emp1 :{emp['emp1']}")
print("-" * 60)
print(f"emp2 :{emp['emp2']}")
print("-" * 60)
print(f"emp3 :{emp['emp3']}")
print("-" * 60)

for key, info in emp.items():
    print(key)
    print("-" * len(key))
    for k, v in info.items():
        print(k + " => " + str(v))
    print("-" * 60)

print("update".center(60, "-"))

emp1 = {'name': 'David', 'age': 34, 'desig': 'MGR', 'gender': 'male', 'salary': 85000}

emp2 = {'name': 'Lisa', 'age': 30, 'desig': 'TL', 'dept': 'FIN', 'gender': 'female',}

print(f"emp1 :{emp1}")
print('-' * 60)
print(f"emp2 :{emp2}")
print('-' * 60)

# requirement - update the values of emp1 with emp2
emp1.update(emp2)

print(f"emp1 :{emp1}")

print("get".center(60, "-"))
emp1 = {'name': 'David', 'age': 34, 'desig': 'MGR', 'dept': 'HR', 'gender': 'male', 'salary': 85000}

print(f"emp1 :{emp1}")

print('-' * 60)
print(f"Name :{emp1.get('name', 'Invalid Key')}")
print(f"Designation :{emp1.get('design', 'Invalid Key')}")
