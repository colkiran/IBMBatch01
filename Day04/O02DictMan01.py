
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))
print("-" * 60)

d2 = {'name': 'sachin', 'age': 32, 'runs': 85, 'oppn':'Aus'}
print(f"d2 :{d2}")
print(type(d2))

print("-" * 60)
d3 = dict(name='Rahul', age=29, runs=45, oppn='pak')
print(f"d3 :{d3}")
print(type(d3))

print("-" * 60)
d4 = dict([('fname','Sachin'), ('lname', 'tendulkar'), ('age', 30), ('runs', 120), ('oppn', 'zim)')])
print(f"d4 :{d4}")
print(type(d4))

# # CRUD Operations
print("Creation".center(60, "-"))
player = {'name': 'Sachin', 'age': 32, 'runs': 60, 'oppn': 'NZL'}
print(f"player :{player}")
print(type(player))

print("read".center(60, "-"))
print(f"Name :{player['name']}")
print(f"runs :{player['runs']}")
print(f"Opponent :{player['oppn']}")

print("-" * 60)
# iterate

for i in player:
    print(i, "=>", player[i])

print("update".center(60, "-"))
player = {'name': 'Sachin', 'age': 32, 'runs': 60, 'oppn': 'NZL'}
print(f"player :{player}")

# insert new key value  into the dictionary
player['year'] = 1998
player['name'] = 'tendulkar'
player['venue'] = 'Eden Park'

print(f"player :{player}")

print("Delete".center(60, "-"))
print(f"player :{player}")

del player['age']
del player['oppn']

print(f"player :{player}")

print("-" * 60)
print(dir(player))