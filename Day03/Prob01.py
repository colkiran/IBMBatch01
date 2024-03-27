
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

print("-" * 60)
for i in range (1, 6):
    for k in range(1, 7-i):
        print(" ", end= "")
    for j in range(1,i+1):
        print(j, end= " ")
    print()

print("-" * 60)
for i in range(1, 6):
    print(" " * (5-i), end="")
    for j in range(1, i+1):
        print(j, end=" ")
    print()