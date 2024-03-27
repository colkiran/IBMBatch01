
"""
sort    - will sort the original list
sorted  - will take a copy of the list, sort it and return it
"""
l1 = [8, 5, 6, 9, 1, 10, 4, 2, 7, 3]
print(f"l1 :{l1}")

l1_asc = sorted(l1)
l1_desc = l1.sort(reverse=True)

print(f"Ascending order :{l1_asc}")
print(f"Descending order :{l1}")

print("-" * 60)
l1 = [8, 'zebra', 5,'apple', 6, 'yellow', 9, 'blue',1, 'x-ray', 10, 'white', 4, 'green', 2, 'violet', 7, 'dog', 3, 'cat', 'pink', 'mango', 198, 1287, 29, 231, 2098]
print(f"l1 :{l1}")

print("-" * 60)
res = sorted(l1, key=ascii)
print(f"res :{res}")

print("-" * 60)
cities = ['vishakapatnam', 'delhi', 'thiruvananthapuram', 'bangalore', 'chennai', 'pune', 'hyderabad', 'mumbai', 'ooty']
print(f"cities :{cities}")

print("-" * 60)
cities_asc = sorted(cities, key=len)
cities_desc = sorted(cities, key=len, reverse=True)

print(f"Ascending order :{cities_asc}")
print("-" * 60)
print(f"Descending order :{cities_desc}")

print("reversed".center(60, "-"))
l1 = [8, 5, 6, 9, 1, 10, 4, 2, 7, 3]
print(f"l1 :{l1}")

print(list(reversed(l1)))