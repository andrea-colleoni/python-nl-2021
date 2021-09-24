# liste
lista = [1, 2, 3, 4, 5, 6, 'ciao', 'pippo']
print(type(lista))

lista.append(10)
print(lista)
lista.append([20, 21, 22])
print(lista)
lista2 = lista + [20, 21, 22]
print(lista2)
lista3 = [1, 2, 3].append(4)
print(lista3) # non restuisce nulla
print(type(lista3))
print(lista[0]) # index iniziale è 0
print(lista[-1]) # index iniziale è 0

# slice
numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# numeri[from:to:step]
print(numeri[3::])
print(numeri[1:5:2])
pari = numeri[1::2]
print(pari)
numeri.reverse() # inverte
pari = numeri[::2]
print(pari)

# riferimenti
v1 = [1, 2, 3]
v2 = v1 # sto copiando il puntaore (reference) della lista
v1.append(4)
print(v2) # v2 e v1 puntano alla stessa area di memoria
v2 = v1[:] # copiare i valori di una lista

del v1[2] # rimuove un elemento
print(v1)
print(v1.index(4)) # ricerca di un elemento
print(5 in v1)
print(len(v1))
print(len('abcdefhijkl'))
print('abcdefhijkl'[5:10:]) # la stringa è una lista di caratteri