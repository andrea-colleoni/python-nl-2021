class Cliente:
    ragionesociale = ''
    piva = ''
    indirizzo = ''
    mail = ''
    abilitato = True

    def inviaPec(self):
        print(f'mail inviata a {self.mail}')
    
    def abilita(self):
        self.abilitato = True

    def disabilita(self):
        self.abilitato = False