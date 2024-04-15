
import numpy as np

print("numpy version :", np.__version__)

arr = np.array([1, 2, 3, 4, 5, 6])

print(f"arr :{arr}")

print(type(arr))

# array dimensions
print('Zero Dimension'.center(60, "-"))

arr = np.array(60)

print(arr)

print(f"Dimension :{arr.ndim}")

print("One Dimension".center(60, "-"))

arr1 = np.array([1, 2, 3, 4, 5])

print(f"arr1 :{arr1}")

print(f"Dimension :{arr1.ndim}")

print("Two Dimension".center(60, "-"))

arr2  = np.array([[1, 2, 3], [4, 5, 6]])

print(f"arr2 :\n{arr2}")

print(f"Dimension :{arr2.ndim}")

print("Three Dimension".center(60, "-"))

arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(f"arr3 :\n{arr3}")

print(f"Dimension :{arr3.ndim}")

