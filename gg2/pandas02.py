import pandas as pd

# dati = [1, 2, 3, 4, 5]
dati = [['lun', 27], ['mar', 28], ['mer', 29]]
colonne = ['giorno', 'data']
df = pd.DataFrame(dati, columns = colonne)
print(df)
df.to_csv('calendario.csv')

iris = pd.read_csv('IRIS.csv')
iris.head()
'''
print(iris)
print(iris.axes)
print(iris.values)
print(iris.size)
print(iris.head(10))
print(iris.tail(10))
'''
print(iris.dtypes)
print(iris.ndim)
print(iris.shape)
