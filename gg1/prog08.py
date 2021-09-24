def somma(a, b):
    print(f'a: {a}, b: {b} => {a + b}')
    # print(0/0)
    return {a, b, a + b}

#somma(10, 20)
a, b, s = somma(10, 20)
print(s)

def stackOverflow():
    stackOverflow()

def argomenti(*molti):
    print(type(molti))
    for m in molti:
        print(m)

argomenti(1, 2, 3, 4)


# def argomentiNominati(chiavi):
def argomentiNominati(*altro, **chiavi):    
    """Funzione che accetta un dictionary"""
    print(type(chiavi))
    print(type(altro))
    print(altro)
    for k in chiavi.keys():
        print(f'k: {k}, v: {chiavi[k]}')

argomentiNominati((10, 20, 30), (100, 200, 300), nome='Andrea', cognome='Colleoni', citta='BG')
# argomentiNominati({'nome':'Andrea', 'cognome':'Colleoni', 'citta':'BG'})