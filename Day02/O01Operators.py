
"""
Arithmetic
Augmentor
"""

print("Comparison Operator".center(60, "-"))
# ==, !=, >, >=, <, <=

print(1 == 1)
print(2 == 1)

a = 10
b = 12
print(f"a = {a}\tb = {b}")
print(f"a > b = {a > b}")
print(f"a < b = {a < b}")
print(f"a == b = {a == b}")

print("Logical Operators".center(60, "-"))
# and, or, not

print(1 == 1 and 2 == 2)
print(1 == 1 and 1 == 2)
print("-" * 60)

print(1 == 1 or 2 == 2)
print(1 == 1 or 1 == 2)
print("-" * 60)

print(not(1 == 1 or 1 == 2))
print(not(1 == 2 or 2 == 1))
print("-" * 60)

print(f"a = {ord('a')}")    # integer representation of unicode character
print(f"z = {ord('z')}")
print(f"A = {ord('A')}")
print(f"Z = {ord('Z')}")
print("-" * 60)
print(f"apple > orange :{'apple' > 'orange'}")
print(f"orange > apple :{'orange' > 'apple'}")

print("Bitwise Operators".center(60, "-"))

print(f"5 | 3 :{5 | 3}")
print(f"5 & 3 :{5 & 3}")
print(f"5 ^ 3 :{5 ^ 3}")
print(f"5 << 1 :{5 << 1}")
print(f"8 << 1 :{8 << 1}")
print(f"16 >> 1 :{16 >> 1}")

print(f"5 >> 1 :{5 >> 1}")

print("Ternary Operator".center(60, "-"))
a = 20
print("Eligible" if a >= 18 else "Not Eligible")

