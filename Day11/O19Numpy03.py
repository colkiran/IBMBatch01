import numpy
import numpy as np

arr = numpy.array([1, 2, 3, 4, 5])

print(f"arr :{arr}")

print(f"arr[1:5:2] :{arr[1:5:2]}")

print(f"arr[::2] :{arr[::2]}")

print("-" * 60)

arr1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(f"arr1 :\n{arr1}")

print(f"arr1[1, 1:4] :{arr1[1, 1:4]}")
print()

print(f"arr1[0:2, 1:4] :\n{arr1[0:2, 1:4]}")
print()

print(f"arr1[0:2, 2] :\n{arr1[0:2, 2]}")
