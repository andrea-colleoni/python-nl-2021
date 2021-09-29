## classi

class Human:
    # campi (fields)
    # convenzione per una COSTANTE
    SPECIE = 'Homo sapiens'
    # campo normale (accessibile in r/w)
    nome = ''
    # convenzione per un campio _privato
    # (che non dovrebbe essere modificato al di fuori di questa classe)
    _eta = 0
    
    def __init__(self, nome):
        self.nome = nome

    def scrivi(self):
        print(self.nome)
    
    @staticmethod
    def stampaInfo():
        print('questa è la classe Human')

    # accesso in sola lettura ad un field
    @property
    def eta(self):
        return self._eta

    @eta.setter
    def eta(self, eta):
        if (eta < 0):
            raise Exception("L'età non può essere negativa")
        self._eta = eta

class Supereroe(Human):
    superpotere = 'Volare'