# set
# come le liste ma senza duplicati (unique)

s1 = {-1, 1, 2, 2, 3, 3, 3, -5, 4}
print(s1)
s2 = {9, 8, 3, False, 4, 5, 'ciao', 7, True}
print(s2.intersection(s1))

# unione
print(s1 | s2)
# intersezione
print(s1 & s2)
print('ciao')
# differenza
print(s1 - s2)
print(s2 - s1)