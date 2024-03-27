
print("copy".center(60, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 before :{l1}")

# copy the list l1 to l2
l2 = l1         # shallow copy  - copying the data with the address

print(f"l2 before :{l2}")
l2.append(6)
l2.append(7)
l2.append(8)
l2.append(9)

print(f"l2 after :{l2}")
print(f"l1 after :{l1}")

print("=" * 60)
# COPY
l3 = list(range(5, 31, 5))
print(f"l3 before :{l3}")

# copy the list l3 to l4
l4 = l3.copy()          # deep copy - only the data is copied
print(f"l4 before :{l4}")

l4.extend([35, 40, 45, 50])
print(f"l4 after :{l4}")
print(f"l3 after :{l3}")

print("=" * 60)
# flaw in the copy function
l5 = [2, 4, 6, 8, [3, 5, 7, 9], 10, 12]
print(f"l5 before :{l5}")

# copy the list l5 to l6
l6 = l5.copy()          # deep copy
print(f"l6 before :{l6}")

l6[4].extend([11, 13, 15])
print(f"l6 after :{l6}")
print(f"l5 after :{l5}")

print("=" * 60)
from copy import deepcopy
l7 = [2, 4, 6, 8, [3, 5, 7, 9], 10, 12]
print(f"l7 before :{l7}")
l8 = deepcopy(l7)
print(f"l8 before :{l8}")

l8[4].extend([11, 13, 15])
print(f"l8 after :{l8}")
print(f"l7 after :{l7}")