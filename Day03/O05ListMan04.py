
# CRUD on List

lst1 = [1, 2, 3, 4, 5]
print(f"lst1 :{lst1}")
print("-" * 60)

print(f"lst1[0] :{lst1[0]}")
print(f"lst1[1] :{lst1[1]}")

print("-" * 60)
for l in lst1:
    print(l, end=" ")
print()

print("-" * 60)
# update or add
print(f"lst1 :{lst1}")

# insert 10 in between 3 an 4
lst1[3] = 10        # replaced
print(f"lst1 :{lst1}")

print("-" * 60)
# delete
print(f"lst1 :{lst1}")
del lst1[3]

print(f"lst1 :{lst1}")

# print("-" * 60)
# print(dir(lst1))
print("Append".center(60, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

# append can insert on value(element) at a time
l1.append(6)
l1.append(7)
l1.append(8)

print(f"after appending :{l1}")
l1.append([9, 10, 11, 12, 13])

print(f"after appending :{l1}")
# print 10, 11, 12
print(l1[8][1:4])

print("Extend".center(60, "-"))
# we can insert more than one value into the list
l2 = [5, 10, 15, 20, 25]
print(f"l2 :{l2}")

l2.extend([30, 35, 40, 45, 50])
print(f"l2 :{l2}")

l2.extend([55])
print(f"l2 :{l2}")

print("Insert".center(60, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

l1.insert(1, 1.5)
l1.insert(3, 2.5)
l1.insert(5, 3.5)
l1.insert(7, 4.5)

print(f"l1 :{l1}")


