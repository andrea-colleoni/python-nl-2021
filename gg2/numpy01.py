import numpy as np

a = np.array([1, 2, 3, 4, 5], dtype = np.int16)
print(a.dtype)
print(type(a))
# copia di puntatori
b = a
# copia
b = np.array(a, copy = True)
print(b)