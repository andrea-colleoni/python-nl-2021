import pandas as pd

poke = pd.read_csv('Pokemon.csv')

# concat
bugs = poke.loc[(poke['Type 1'] == 'Bug')]
grass = poke.loc[(poke['Type 1'] == 'Grass')]

bugs = bugs.reset_index()
grass.reset_index(inplace = True)
# print(bugs)
# print(grass)
poke = pd.concat([bugs, grass])
#print(poke)

# trasposizione
print(poke.T)

# pivot
pivot = poke.pivot(columns=['Type 1', 'Type 2'], values=['Attack', 'Defense'])
# print(pivot)

# dropna, fillna
# eliminare le riche che hanno NA in Attack
poke.dropna(subset=['Attack'], inplace = True)
# print(poke)

# riempire con media attacco gli attachi NA
avgAttck = poke['Attack'].mean()
print(avgAttck)
poke['Attack'].fillna(value = poke['Attack'].mean())

print(poke.head(5))