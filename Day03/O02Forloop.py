

for i in range(1, 10):
    print(i, end=" ")
print()

print("-" * 60)
for i in range(1, 26):
    # if i > 20:
    #     break           # stop or exit the iteration
    if i % 2 == 1:
        continue        # skip the current iteration
    print(i, end=" ")
else:
    print("\nCompleted the iteration of numbers")
print()
