import prog01 as p1

andrea = p1.Human('Andrea')
anna = p1.Human('Anna')
andrea.stampaInfo()

anna.scrivi()

andrea.SPECIE = 'Cane'
andrea.scrivi()

andrea.eta = 18
andrea._eta = -10
print(andrea.eta)

batman = p1.Supereroe('Batman')
print(batman.superpotere)
batman.eta = 50