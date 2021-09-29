import pandas as pd
import numpy as np

iris = pd.read_csv('IRIS.csv')
iris.head()
print('**************************')
# print(iris['species'])
iris['species'] = iris['species'].astype('category')
iris['species_cat'] =  iris['species'].cat.rename_categories(range(1, iris['species'].cat.categories.size + 1))
print(iris)
labels = pd.DataFrame()
labels['specie'] = iris['species']
labels['codice'] = iris['species_cat']
del iris['species']
print(labels)

print('**************************')
print(iris.describe())
#print(iris.apply(np.mean))
