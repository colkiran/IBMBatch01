
s1 = set()
print(f"s1 :{s1}")
print(type(s1))

print("-" * 60)
s2 = {1, 2, 3, 4.2, 5.6, 6.9, 'seven', 'eight', 'nine', 10+1j, 11-3j, True, False}

# True - 1, False - 0
print(f"s2 :{s2}")
print(type(s2))

print("-" * 60)
s3 = set(range(1, 11))
print(f"s3 :{s3}")
print(type(s3))

print("-" * 60)
# print(dir(s1))

s1 = {1, 2, 3}
print(f"s1 :{s1}")

print("add".center(60, "-"))
s1.add(4)
s1.add(1)
s1.add(3)
s1.add(5)
s1.add(2)
s1.add(6)

print(f"s1 :{s1}")

print("update".center(60, "-"))
s1.update([1, 2, 3])
s1.update([5, 6, 7])
s1.update([3, 4, 5])
s1.update([8, 9, 10])
s1.update([7, 8, 9])
print(f"s1 :{s1}")

