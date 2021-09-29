import numpy as np

# array multidimensionale
a = np.array([[1, 2, 3], [4, 5, None]])
print(a)
print(a.shape)
print(a.ndim)

b = a.reshape(3, 2)
print(b)
print(b.ndim)

c = a.reshape(6)
print(c)

print(c.ndim)

d = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 20, 30], [40, 50, 60], [70, 80, 90]]])
print(d)
print(d.ndim)

print(d.itemsize) # dimensione in bytes del singolo item
print(d.size) # numero di items
print(type(d.shape))
print(d.shape)
'''
b = np.array([[1, 2, 3], [4, 5, 6, 7]])
print(b)
print(b.shape)
'''