import numpy as np

a = np.arange(100)
a = a.reshape(25, 4)
np.save('range.py.array', a)
np.savetxt('range.py.array.csv.gz', a, delimiter=';', newline='\n')

'''
b = np.load('range.py.array.npy')
print(b)
'''

b = np.loadtxt('range.py.array.csv.gz', delimiter=';')
print(b)