import numpy as np

# Slicing (Same as Python List)
a = np.array([6, 7, 8])
# print(a[0:2])
# print(a[-1])

a = np.array([[6, 7, 8], [1, 2, 3], [9, 3, 2]])
# print(a[1, 2])
# print(a[0:2, 2])
# print(a[-1, 0:2])
# print(a[:, 1:3])




# Iterate through an array
a = np.array([[6, 7, 8], 
              [1, 2, 3], 
              [9, 3, 2]])

# for row in a:
#     print(row)

# for cell in a.flat:
#     print(cell)




# Stacking
a = np.arange(6).reshape(3, 2) 
b = np.arange(6, 12).reshape(3, 2)
# print(a) 
# print(b) 

# print(np.vstack((a, b)))   # Vertically Stacking
# print(np.hstack((a, b)))   # Horizontally Stacking




# Spliting
a = np.arange(30).reshape(2, 15)
# print(a)
result = np.hsplit(a, 3)   # Horizontal Split
# print(result[0])
# print(result[1])
# print(result[2])

result = np.vsplit(a, 2)   # Vertical Split Split
# print(result[0])
# print(result[1])




# Indexing with Boolean arrays
a = np.arange(12).reshape(3, 4)
print(a)
b = a > 4
print(b)
print(a[b])   # Extracting greater than 4 value from array

a[b] = -1   # True values set into -1
print(a)
