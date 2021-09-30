import pandas as pd

count = 0

for poke_chunk in pd.read_csv('Pokemon.csv', chunksize=100):
    print(poke_chunk.size)
    # print(poke_chunk.describe())

print(count)