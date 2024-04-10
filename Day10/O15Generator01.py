
print(sum([x ** 2 for x in range(1, 11)]))       # comprehension

print(sum(x ** 2 for x in range(1, 11)))           # generator

from sys import getsizeof
val1 = [x ** 2 for x in range(10000)]
print(f"Comprehension size of lst :", getsizeof(val1))

val2 = (x ** 2 for x in range(10000))
print(F"generator size of lst :", getsizeof(val2))
