
print("keys".center(60, "-"))

player = {'name': 'Rahul', 'age': 30, 'runs': 120, 'oppn': 'SA'}
print(f"player :{player}")

k  = player.keys()
print(f"k :{k}")

print("-" * 60)
for k in player.keys():
    print("k", " => ",  player[k])

print("values".center(60, "-"))
player = {'name': 'Rahul', 'age': 30, 'runs': 120, 'oppn': 'SA'}
print(f"player :{player}")

v = player.values()
print(f"v :{v}")

print("fromkeys".center(60, "-"))
# fromkeys is used to convert a list into a dictionary

fruits= ['apple', 'orange', 'grapes', 'pineapple', 'banana']
print(f"fruits :{fruits}")

# convert fruits into a dictionary
prices = dict.fromkeys(fruits)
print(f"prices :{prices}")

prices = dict.fromkeys(fruits, 50)
print(f"prices :{prices}")

print("setdefault".center(60, "-"))
player = {'name': 'Rahul', 'age': 30, 'runs': 120, 'oppn': 'SA'}
print(f"player :{player}")

# setdefault function only adds a new key value pair into the dictionary
player.setdefault('name', "dravid")
player.setdefault('venue', "Chepauk")
player.setdefault('year', 2015)
player.setdefault('runs', 50)

print(f"player :{player}")

print("pop".center(60, "-"))
player = {'name': 'Rahul', 'age': 30, 'runs': 120, 'oppn': 'SA', 'venue': 'Chepauk', 'year': 2015}

print(f"player :{player}")

res = player.pop("runs")
print(f"res :{res}")

res = player.pop("age")
print(f"res :{res}")

# res = player.pop("fname")

print(f"player :{player}")

print("popitem".center(60, "-"))
player = {'name': 'Rahul', 'age': 30, 'runs': 120, 'oppn': 'SA', 'venue': 'Chepauk', 'year': 2015}

print(f"player :{player}")

res = player.popitem()
print(f"res :{res}")

res = player.popitem()
print(f"res :{res}")

print(f"player :{player}")
