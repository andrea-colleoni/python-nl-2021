import numpy as np

a = np.arange(10)
print(a)

print(a[1:8:2])
a = a.reshape(2, 5)
print(a)
print(a[1:,2:])

# si possono passare collezioni di indici per ciascuna dimensione
print(a[[0, 1], [1,2]])

# singolo elemento
print(f'singolo elemento: {a[1, 3]}')

print(a[a > 4]) # condizione boolean


