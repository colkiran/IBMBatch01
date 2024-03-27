
letters = ['a', 'b', 'c', 'd', 'e']
print(f"letters :{letters}")

for letter in letters:
    print(letter, end=" ")
print()     # line break
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
