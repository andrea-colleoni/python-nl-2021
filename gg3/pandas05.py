import pandas as pd
import numpy as np

poke = pd.read_csv('Pokemon.csv')

# group by più colonne e più aggregazioni
maxAttckPerType = poke.groupby(['Type 1', 'Type 2'])
# print(maxAttckPerType)
# print(maxAttckPerType['Attack'].max())
# print(maxAttckPerType['Defense'].min())

# modo 1
print(maxAttckPerType.agg({'Attack': ['max'], 'Defense': [np.min, np.sum]}))
# modo 2
print(maxAttckPerType.aggregate(AMax=pd.NamedAgg(column='Attack', aggfunc='max'), DMin = pd.NamedAgg(column='Defense', aggfunc='min')))