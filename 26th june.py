a = np.array([1, 2, 3, 4, 5, 6])
print(a.shape)  

# Reshape to a 2D array
b = a.reshape(2, 3)
print(b)

# Reshape to a 3D array
c = a.reshape(2, 1, 3)
print(c)
(6,)
[[1 2 3]
 [4 5 6]]
[[[1 2 3]]

 [[4 5 6]]]
 

 a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Concatenate along a new axis (stacking)
c = np.stack((a, b))
print(c)

# Concatenate along an existing axis (horizontal)
d = np.concatenate((a, b), axis=None)
print(d)  

# Concatenate along an existing axis (vertical)
e = np.array([[1, 2], [3, 4]])
f = np.array([[5, 6], [7, 8]])
g = np.concatenate((e, f), axis=0)
print(g)