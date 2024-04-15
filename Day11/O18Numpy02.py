
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(f"arr[1] :{arr[1]}")

print(f"arr[1] + arr[3] = {arr[1] + arr[3]}")

print("2 D".center(60, "-"))
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(f"arr :\n{arr}")

print(f"arr[0, 2] :{arr[0, 2]}")
print(f"arr[1, 3] :{arr[1, 3]}")

print("3 D".center(60, "-"))
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(F"arr :\n{arr}")

print(f'arr[0, 1, 2] :{arr[0, 1, 2]}')
print(f'arr[1, 1, 2] :{arr[1, 1, 2]}')
