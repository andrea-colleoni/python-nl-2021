d = {'chiave': 10, 'altro': 11}
print(d)
print(type(d))
try:
    print('ok')
    print(d['nonesiste'])
    # istruzioni.....
    print('dopo eccezione')
except KeyError as ke:
    print(ke)
except Exception as err:
    print('si è verificato un problema')
    print(type(err))

print('finito')