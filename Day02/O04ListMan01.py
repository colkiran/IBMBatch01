
l1 = list()
print(f"l1 :{l1}")
print(type(l1))
print("-" * 60)

l2 = [1, 2, 3, 4.5, 5.2, 6.1, 'seven', 'eight', 'nine', True, False, 12+0j, 13-2j]
print(f"l2 :{l2}")
print(type(l2))
print("-" * 60)

l3 = list(range(1, 11))
print(f"l3 :{l3}")
print(type(l3))
print("-" * 60)

values = list(range(10, 40, 10))
print(f"values :{values}")

# unpack the list
a, b, c = values
print(a, b, c, sep=", ")
print("-" * 60)

values = list(range(10, 101, 10))
print(f"values :{values}")

a, b, *c = values       # c can accept more than one value
print(a, b, c, sep=", ")
print("-" * 60)

*a, b, c = values
print(a, b, c, sep=", ")
print("-" * 60)

a, *b, c = values
print(a, b, c, sep=", ")
print("-" * 60)

lst1 = [1, 2, 3, 4, 5]
lst2 = [11, 22, 33, 44, 55]

print(f"lst1 :{lst1}")
print(f"lst2 :{lst2}")

lst3 = [lst1, lst2]
print(f"lst3 :{lst3}")
print(len(lst3))
print("-" * 60)

lst4 = [*lst1, *lst2]       # unpack the elements of the list
print(f"lst4 :{lst4}")
print(len(lst4))
