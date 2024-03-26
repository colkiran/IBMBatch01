
"""
1. int
2. float
3. complex
"""

a = 1
b = -1
print(f"a :{a}")
print(type(a))          # RTTI - runtime type indentification
print(f"b :{b}")
print(type(b))

print("-" * 60)
c = 1.0
d = -1.0
print(f"c :{c}")
print(type(c))
print(f"d :{d}")
print(type(d))
print("-" * 60)

e = +2e3
f = -2e3
print(f"e :{e}")
print(type(e))
print(f"f :{f}")
print(type(f))
print("-" * 60)

g = 3.141j
h = -3.141j
print(f"g :{g}")
print(type(g))
print(f"h :{h}")
print(type(h))

print("-" * 60)
print(max(10, 15, 8, 6, 1, 13))
print(min(10, 15, 8, 6, 1, 13))

print("-" * 60)
x = 2 + 3.5
print(f"x :{x}")
print(type(x))

x = 1
y = 2.5
z = x + y
print("x = ", type(x))
print("y = ", type(y))
print("z = ", type(z))

print("Conversion".center(60, "-"))
a = 100
print(f"a :{a}")
print(f"{type(a)}\t\t{a}")
print(f"{type(float(a))}\t\t{float(a)}")
print(f"{type(complex(a))}\t\t{complex(a)}")
print(f"{type(bool(a))}\t\t{bool(a)}")

print("Number System".center(60, "-"))
print(f"11 :{11}")          # decimal
print(f"0b11 :{0b11}")      # binary
print(f"0b101 :{0b101}")    # binary
print(f"0o11 :{0o11}")      # octal
print(f"0o101 :{0o101}")    # octal
print(f"0xe :{0xe}")        # hexa
print(f"0xa :{0xa}")        # hexa

print("Number System Conversion".center(60, "-"))
a = 100
print(bin(a))
print(oct(a))
print(hex(a))