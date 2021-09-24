# byref, byval

def f(p):
    p[0] = p[1] * 2

l = [10, 20, 30]
f(l)
print(l)

def somma(a, b):
    a *= 20

a = 10
somma(a, 10)
print(a)
l = [a]
somma(l, 10)
print(l)

# funzioni anonime

lambda x: x**2 

def sq(x):
    return x**2

def creaIncrementatoreDi(n):
    return lambda x: x + n, lambda x: x + (n+1)

def usaIncrementatore(inc, x):
    return inc(x)

inc2, inc3 = creaIncrementatoreDi(2)
print(inc2(10))

ris = usaIncrementatore(inc2, 20)
print(ris)