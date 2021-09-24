# dictionary
d = {'chiave': 10, 'altro': 11}
print(d)
print(type(d))
print(d['altro'])
#print(d['nonesiste'])
print(d.get('nonesiste'))
for k in d.keys():
    print(d[k])
for v in d.values():
    print(v)

d.update({ 'nuovo': 20})
print(d)
d.update({'nuovo': 30})
print(d)
'''
for k in d.keys():
    d.update({ k + '_': 10}) # non si può
    print(d)
'''
for k in d.keys():
    d.update({ k: 10}) 
    print(d)

d.setdefault('default', 100)
print(d)

del d['altro']
print(d)

# esempio di swap usando unpack
a = 10
b = 20
print(f'a: {a}, b: {b}')
a, b = b, a
print(f'a: {a}, b: {b}')