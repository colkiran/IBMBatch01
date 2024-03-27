
st1 = "hello world"
st2 = "the quick brown fox jumps over the lazy dog"

print("find".center(60, "-"))
print(f"st1 :{st1}")
pos = st1.find("l")
print(f"Index :{pos}")

pos = st1.find("l", st1.find("l") + 1)
print(f"Index :{pos}")

pos = st1.find("l", st1.find("l", st1.find("l") + 1) + 1)
print(f"Index :{pos}")

print("-" * 60)
print(f"st2: {st2}")
pos = st2.find("the")
print(f"Index :{pos}")

pos = st2.find("the", st2.find("the") + 1)
print(f"Index :{pos}")

print("-" * 60)
print("Replace".center(60, "-"))
print(f"st1 :{st1}")
res1 = st1.replace("h", "H")
print(f"After replacing :{res1}")

print("-" * 60)
res1 = st1.replace("l", "L")
print(f"After replacing :{res1}")

res1 = st1.replace("l", "L", 1)
print(f"After replacing :{res1}")

res1 = st1.replace("l", "L", 2)
print(f"After replacing :{res1}")
print("-" * 60)

print("Index".center(60, "-"))
print(f"st1 :{st1}")
idx = st1.index("w")
print(f"index of w:{idx}")

print("-" * 60)
idx = st1.index("l")
print(f"index of l:{idx}")

idx = st1.index("l", st1.index("l") + 1)
print(f"index of l:{idx}")

# maketrans and translate
st = "hello world"
print(f"st :{st}")

# convert st from lower case to upper case
a = "helowrd"
b = "HELOWRD"
resTbl = st.maketrans(a, b)
print(f"result :{resTbl}")

res = st.translate(resTbl)
print(f"results :{res}")

