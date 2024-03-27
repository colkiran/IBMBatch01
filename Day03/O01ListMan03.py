
letters = ['a', 'b', 'c', 'd', 'e']
print(f"letters :{letters}")

print("-" * 60)

for letter in letters:
    print(letter, end=" ")
print()         # line  break

print("-" * 60)
for letter in enumerate(letters):
    print(letter, end=" ")
print()

print("-" * 60)
for letter in enumerate(letters):
    print(letter[0], letter[1])

print("-" * 60)
for index, letter in enumerate(letters):
    print(index, letter)

print("-" * 60)

mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"mylist :{mylist}")

print("-" * 60)
for list in mylist:
    print(list)

print("-" * 60)
for index, lst in enumerate(mylist):
    print(f"{index}\t {lst}")

print("-" * 60)
# for index, lst in enumerate(mylist):
#     print(f"\n{index}")
#     for ind, l in enumerate(lst):
#         print(f"{ind} \t {l}")

for index, sublist in enumerate(mylist):
    print("Index:", index)
    for value_index, value in enumerate(sublist):
        print("Value at Index", value_index, ":", value)