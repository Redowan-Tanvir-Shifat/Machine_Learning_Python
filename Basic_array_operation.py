import numpy as np

# a1 = np.array([2, 6, 9])
# a2 = np.array([1, 3, 3])

# print(a1 + a2)
# print(a1 - a2)
# print(a1 * a2)
# print(a1 / a2)


# a = np.array([5, 6, 7])   # 1D array
# print(a)

# a = np.array([[1, 2], [3, 4], [4, 5]])
# a = np.array([[1, 2], [3, 4], [4, 5]], dtype=int)   # set the datatype
# print(a.ndim)   # for check dimension of the array
# print(a.itemsize)
# print(a.dtype)
# print(a)
# print(a.size)
# print(a.shape)   # rows and column


# a = np.array([[1, 2], [3, 4], [4, 5]], dtype=complex)
# print(a)

# print(np.zeros( (3, 4) ))   # all initialized with zero
# print(np.ones( (3, 4) ))   # all initialized with one

# print(np.arange(1, 5))   # list like lists range function
# print(np.arange(1, 5, 2))   # last perameter is number of step to reach 5
# print(np.linspace(1, 5, 10))   # this function generates 10 numbers between 1 to 5 which are linearly spaced

# a = np.array([[1, 2], [3, 4], [4, 5]])
# print(a)
# print(a.shape)
# print(a.reshape(2, 3)) 
# print(a.ravel())   # make the 2D array flat (1D)
# print(a.min())
# print(a.max())
# print(a.sum())   # sum all the elemnt
# print(a.sum(axis=0))   # sum of column
# print(a.sum(axis=1))   # sum of rows
# print(np.sqrt(a))   # sqrt is a 'Generic Funtion'
# print(np.std(a))

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)

print(a.dot(b))  # matrix product 
print(np.dot(a, b))  # matrix product another way 
