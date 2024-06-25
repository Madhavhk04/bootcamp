
# 1D array
a = np.array([10, 20, 30, 40, 50])
print(a.shape)

# 2D array
b = np.array([[11, 22, 33], [44, 55, 66]])
print(b.shape)

# 3D array
c = np.array([[[10, 20], [30, 40]], [[50, 60], [70, 80]]])
print(c.shape)


import numpy as np
import time

# Create large arrays with new random values
a = np.random.rand(5000000)
b = np.random.rand(5000000)

# Element-wise operations in NumPy
start = time.time()
c = a + b
end = time.time()
print(f"NumPy element-wise addition took: {end - start:.6f} seconds")

# Element-wise operations in Python lists with new values
start = time.time()
x = [i * 2 for i in range(5000000)]
y = [i * 3 for i in range(5000000)]
z = [x[i] + y[i] for i in range(5000000)]
end = time.time()
print(f"Python list element-wise addition took: {end - start:.6f} seconds")
