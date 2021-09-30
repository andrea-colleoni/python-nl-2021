import pandas as pd

poke = pd.read_csv('Pokemon.csv')

#print(poke.head(10))
print(poke[['Name', 'Type 1', 'Type 2']])
print(poke.iloc[0:4])
'''
for idx, riga in poke.iterrows():
    # riga: è una pandas Series
    print(f'Indice: {idx}:\n')
    print(riga['Name'])
    print('-----------------------------------')
'''

filtro = (poke['Type 1'] == 'Grass') & ~(poke['Type 2'] == 'Poison') # è un array di bool
poke = poke.loc[filtro]
# poke.loc[filtro]

poke.sort_values(['Attack', 'Defense'], inplace = True, ascending = [True, False])
print(poke)

