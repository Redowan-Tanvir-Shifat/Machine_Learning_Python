import numpy as np
import sys
import time

a = np.array([1, 2, 3])
print(a)
print(a[0])

l = range(1000)
print(sys.getsizeof(5) * len(l))

array = np.arange(1000)
print(array.size * array.itemsize)


# Time check for run the task between Python list and Numpy Array
SIZE = 1000000

l1 = range(SIZE)
l2 = range(SIZE)

a1 = np.array(SIZE)
a2 = np.array(SIZE)

# Python list
start = time.time()
result = [(x+y) for x, y in zip(l1, l2)]   # adding l1 and l2 in result
print("Python took in list: ", (time.time() - start) * 1000)

# Numpy array
start = time.time()
result = a1 + a2   # also convinient
print("Python took in numpy: ", (time.time() - start) * 1000)

