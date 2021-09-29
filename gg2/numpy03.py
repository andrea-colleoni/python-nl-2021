import numpy as np
# creazione di ndarray

# partendo da una lista
a = np.array([1, 2, 3])
print(a)

# vuoto
b = np.empty([3, 4], dtype = np.int16)
print(b)

# zeri
c = np.zeros([5, 4], dtype = np.float)
print(c)
print(c.dtype)

# uno
d = np.ones([2, 3], dtype = np.int16)
print(d)

# da collezioni esistenti (qualsiasi tipo di collezione)
e = np.asarray([1, 2, 3, 4, 5])
print(e)
print(e.shape)

# da un oggetto iterabile
r = range(100)
it = iter(r)
f = np.fromiter(it, dtype = np.int16)
f = f.reshape(4, 25)
print(f)