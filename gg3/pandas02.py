import pandas as pd

poke = pd.read_csv('Pokemon.csv')

#print(poke['Attack'] - poke['Defense'])
poke['Diff'] = poke['Attack'] - poke['Defense']
#poke['Name'] = poke['Name'].astype('str')
poke['Upper Name'] = poke['Name'].str.upper()
poke['IsMega'] = poke['Name'].str.contains('Mega')

bugs = poke.loc[poke['Type 1'] == 'Bug']
bugs.to_excel('bugs.xlsx')

# broadcast di uno scalare su una colonna
poke['Max Attack'] = poke['Attack'].max()
poke.drop(labels=['HP'], inplace = True, axis = 1)

# groupby e max()
maxAttckPerType = poke.groupby(['Type 1'])['Attack'].max()
poke = poke.merge(maxAttckPerType, on = 'Type 1')

print(poke.head(10))