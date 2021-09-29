import pandas as pd
import numpy as np

# pandas DataFrame è una tabella 2D con titoli sulle colonne
# ha colonne di tipo eterogeneo

# pandas Serie è un array 1D

data = np.array([1, 2, 3, 4, 5, 6])
s = pd.Series(data)
print(s)
print(type(s))
ggl = ['lu', 'ma', 'me', 'gi', 've', 'sa', 'do']
gg = ['lunedì', 'mart', 'merc', 'gio', 'ven', 'sab', 'dom']
week = pd.Series(gg, dtype = str, index = ggl)
print(week)
print(week[2:5])
print(type(week['lu']))