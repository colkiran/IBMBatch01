
st = "hello world"
print(f"st :{st}")
print(type(st))
# print(dir(st))
print("-" * 60)

print(f"st[0] :{st[0]}")
print(f"st[6] :{st[6]}")
print(f"st[10] :{st[10]}")
print("-" * 60)

# slicing
print(f"st[0:5]  :{st[0:5]}")
print(f"st[6:11] :{st[6:11]}")
print(f"st[0:11] :{st[0:11]}")
print(f"st[:11]  :{st[:11]}")
print(f"st[0:]   :{st[0:]}")
print(f"st[:]    :{st[:]}")
print("-" * 60)

# reverse indexing
print(f"st[-1]  :{st[-1]}")
print(f"st[-5]  :{st[-5]}")
print(f"st[-11] :{st[-11]}")
print("-" * 60)

# slicing
print(f"st[-1:-6:-1]  :{st[-1:-6:-1]}")
print(f"st[-7:-12:-1] :{st[-7:-12:-1]}")
print(f"st[-1:-12:-1] :{st[-1:-12:-1]}")
print(f"st[:-12:-1]   :{st[:-12:-1]}")
print(f"st[-1::-1]    :{st[-1::-1]}")
print(f"st[::-1]      :{st[::-1]}")
print("-" * 60)

st = "hello"
print(f"st :{st}")
print(f"st[0] :{st[0]}")
# st[0] = "H"    - immutable
print("-" * 60)

# to manipulate strings we have to make use of functions
st = "hello world"
print(f"st :{st}")

uc = st.upper()
tc = st.title()
print(f"upper case :{uc}")
print(f"title case :{tc}")
print("-" * 60)

# Question
st = "Bhargavi12345"
res = "najaragan54321"

st1 = ""
st2 = ""
for i in st:
    if i.isdigit():
        st2 += i
    else:
        st1 += i

print(st1)
print(st2)
print(st1[::-1]+st2[::-1])
