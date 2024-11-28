import numpy as np

a = np.arange(12).reshape(3, 4)
# print(a)


# Same 
# for row in a:
#     for cell in row:
#         print(cell)

# for cell in a.flatten():
#     print(cell)



# for x in np.nditer(a, order = 'C'):
#     print(x)   # row by row

# for x in np.nditer(a, order = 'F'):
#     print(x)   # column by column

# for x in np.nditer(a, order = 'F', flags = ['external_loop']):
#     print(x)   # column by column

for x in np.nditer(a, op_flags=['readwrite']):
    x[...] =x*x   # sq 
print(a)

b = np.arange(3, 15, 4).reshape(3, 1)
print(b)

for x, y in np.nditer([a, b]):
    print(x, y)