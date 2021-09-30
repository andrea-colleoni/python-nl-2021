import pandas as pd

# leggere xls
# dare i nomi alle colonne
def leggiDati(nomefile):
    colonne = ['Area Manager', 'Agente', 'Referenza', \
        'P24', 'P23', 'P22', 'P21', 'P20', \
            'P19', 'P18', 'P17', 'P16', 'P15', 'P14', 'P13', 'P12', 'P11', 'P10', \
            'P09', 'P08', 'P07', 'P06', 'P05', 'P04', 'P03', 'P02', 'P01'    ]
    df = pd.read_excel(nomefile, header = None, names = colonne, sheet_name = 0)
    return df

def leggiMappa(nomefile):
    colonne = ['Referenza', 'Nome prodotto', 'Brand' ]
    df = pd.read_excel(nomefile, header = None, names = colonne, sheet_name = 1)
    return df 



# pulitura dati: (trim, replace spazi e _, fill (o drop) na)
# determinazione della percentuale di missing values
def pulisciColonna(dati, colonna):
    return dati[colonna].str.strip()

def pulisciDati(dati):
    #trim
    daPulire = ['Area Manager', 'Agente', 'Referenza']
    for col in daPulire:
        dati[col] = pulisciColonna(dati, col)

# creare aggregati di colonne (somme) 12 a 12
# calcolare le quote
# calcolare KPI

# trasporre il dato
# generare una serie di tipo temporale

# esportare
nomefile = 'esempio flusso dati.xlsx'
dati = leggiDati(nomefile)
mappa = leggiMappa(nomefile)

pulisciDati(dati)
print(dati)