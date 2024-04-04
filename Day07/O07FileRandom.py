
FL = open("data.txt", "rb")

pos = FL.seek(10, 0)
print(pos)

pos = FL.seek(35, 1)
print(pos)

pos = FL.seek(-25, 1)
print(pos)

pos = FL.seek(100, 2)   # total file size + 100 bytes
print(pos)

pos = FL.seek(0, 2)     # EOF - size of your file
print(pos)

# pos = FL.seek(-10, 0)
# print(pos)

FL.close()