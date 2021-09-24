'''
print('hello')
print("hello")
'''

# print('''ciao,
# io sono Andrea.''')

# variabili
a = 10
print(type(a))
testo = 'ciao'
print(type(testo))
# print e input
print(a)
# scelta = input('inserisci un numero:')
# print(type(scelta))
# concatenazione
# print('hai digitato ' + scelta)
# print('hai digitato {} con la tastiera e la variabile vale {}'.format(scelta, a))
testoDaFormattare = '''Ciao io sono {0}, e sto seguendo il corso di {1}. 
{1} è un linguaggio che piace molto a {0}'''
testoDaFormattare = testoDaFormattare.format('Andrea', 'Python')
print(testoDaFormattare)

testoDaFormattare = '''Ciao io sono {nome}, e sto seguendo il corso di {linguaggio}. 
{nome} è un linguaggio che piace molto a {linguaggio}'''
dict = { 'nome': 'Gigi', 'linguaggio': 'Java'}
testoDaFormattare = testoDaFormattare.format(nome='Andrea', linguaggio='Python')
# testoDaFormattare = testoDaFormattare.format(dict) # così non funziona!!
print(testoDaFormattare)

nome = 'Marco'
linguaggio = 'C#'
print(f'''Ciao io sono {nome}, e sto seguendo il corso di {linguaggio}. 
{nome} è un linguaggio che piace molto a {linguaggio}''')
print('tEsTo'.upper())
print('tEsTo'.lower())
print('testo'.ljust(20, '*'))
print('   testo    '.strip()) # lstrip, rstrip
print('testo1'.isalpha()) # isalnum, isspace, isdecimal