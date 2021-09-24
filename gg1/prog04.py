# tuple
tupla = (0, 10, 20, 30, 40)
print(tupla)
print(type(tupla))
print(tupla[0])
for el in tupla:
    print(el)

# unpacking
_, a, b, c, _ = tupla
print(f'a: {a}, b: {b}, c: {c}')

l = [1, 2, 3]
a, b, c = l
print(f'a: {a}, b: {b}, c: {c}')

# None
a = None
