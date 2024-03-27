
print("pop".center(60, "-"))
l1 = list(range(1, 11))
print(f"l1 :{l1}")

res = l1.pop(7)
print(f"res :{res}")
print(f"l1 :{l1}")

res = l1.pop(3)
print(f"res :{res}")
print(f"l1 :{l1}")

res = l1.pop()
print(f"res :{res}")
print(f"l1 :{l1}")

print("remove".center(60, "-"))
l1 = [1, 2, 2, 2, 1, 1, 1, 2, 3, 1, 2, 1, 1, 1, 1, 1, 2, 3, 1, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 1, 1, 2, 2, 2, 1]
print(f"l1 :{l1}")

l1.remove(3)
print(f"l1 :{l1}")

l1.remove(3)
print(f"l1 :{l1}")

l1.remove(3)
print(f"l1 :{l1}")

print("clear".center(60, "-"))
l2 = list(range(1, 11))
print(f"l2 :{l2}")

l2.clear()      # deletes all the values in the list
print(f"l2 :{l2}")

print("count".center(60, "-"))
l1 = [1, 2, 2, 2, 1, 1, 1, 2, 3, 1, 2, 1, 1, 1, 1, 1, 2, 3, 1, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 1, 1, 2, 2, 2, 1, 2]
print(f"l1 :{l1}")

print(f"1 :{l1.count(1)}")
print(f"2 :{l1.count(2)}")
print(f"3 :{l1.count(3)}")
print(f"5 :{l1.count(5)}")

print("index".center(60, "-"))
l1 = [1, 2, 2, 2, 1, 1, 1, 2, 3, 1, 2, 1, 1, 1, 1, 1, 2, 3, 1, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 1, 1, 2, 2, 2, 1, 2]
print(f"l1 :{l1}")

print(l1.index(3))
print(l1.index(3, l1.index(3) + 1))
print(l1.index(3, l1.index(3, l1.index(3) + 1) + 1))
