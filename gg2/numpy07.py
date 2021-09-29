import numpy as np
import numpy.ma as ma

a = ma.arange(6).reshape((2, 3))
print(a)
a[1, :] = ma.masked
print(a)
print('------------------------------')
b = np.arange(24)
b = b.reshape(6, 4)
rowsum = b.sum(1)
colsum = b.sum(0)
print(rowsum)
# 
print(b[rowsum > 30, :])
valori = np.array([10, 20, 10, 20, 10, 20])
print(b[valori > 10, :])

c = np.array([1, 2, np.NaN, np.NaN, 4])
print(c)