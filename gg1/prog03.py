# controllo di flusso
a = 10
# branching
if a < 20:
    print('minore')
elif a > 40:
    print('troppo grande')
else:
    print('è tra 20 e 40')

# loop
lista = [1, 2, 3, 4, 5, 6]
for numero in lista:
    print(f'sono arrivato a {numero}')
    print('....')
print('*****')
# range(from, to, step)
for n in range(10, 50, 5):
    print(n)

numeri = range(1000000)
print(numeri)
print(type(numeri))

while a > 0:
    print(a)
    a -= 1 # operatore in accumulazione

# matematici: +, -, * , /, //, %, **
# di confronto: <, >, <=, >=, ==, !=
# logici: ! (NOT), & (AND), | (OR)

print(10 // 3)
print(10 % 3)