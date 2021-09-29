import numpy as np
from matplotlib import pyplot as plt

x = np.arange(1, 11)
y1 = 2 * x + 5

plt.title('Esempio matplotlib')
plt.xlabel('asse x')
plt.ylabel('asse y')
plt.plot(x, y1, 'y*')
y2 = 2 * x **2 + 3 * x + 1
plt.plot(x, y2, 'b+')
plt.show()