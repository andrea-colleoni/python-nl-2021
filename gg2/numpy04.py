import numpy as np

# np.arange(start, stop, step)
a = np.arange(5)
print(a)
b = np.arange(10, 99)
print(b)
c = np.arange(0, 100, 5)
print(c)

# lineare
d = np.linspace(0, 20, 40, True, dtype = float)
print(d)

# log
e = np.logspace(0, 20, 40, True, 2, dtype= float)
print(e)

# random
f = np.random.rand(3, 5)
print(f)
# operazioni sugli ndarray (tutti gli operatori matematici)
f *= 4
print(f)
b //= 7 # se non ottengo interi (b ha dtyoe = int) => exception
print(b)

