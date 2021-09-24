a = 10
b = 20

def somma(a, b):
    """Somma due numeri dopo aver incrementato il primo di 2 unità"""
    a += 2
    return a + b

def sharedSomma(b):
    global a
    a += 2
    return a + b

print(somma(5, 8))
print(somma(a, b))
print(sharedSomma(b))