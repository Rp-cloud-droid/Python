import numpy as np
# Create a 1D array
arr = np.array([1, 2, 3, 4, 5])
print("Original array:", arr)

# Access elements
print("Element at index 2:", arr[2])
print("Slice from index 1 to 3:", arr[1:4])

# Array operations
print("Array +5:", arr + 5)
print("Array *2:", arr * 2)

# Aggregations
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Max:", np.max(arr))
print("Min:", np.min(arr))