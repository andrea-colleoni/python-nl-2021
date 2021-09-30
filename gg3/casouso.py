import pandas as pd
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta

# leggere xls
# dare i nomi alle colonne
def leggiDati(nomefile):
    colonne = ['Area Manager', 'Manager', 'Prodotto', \
        'P24', 'P23', 'P22', 'P21', 'P20', \
            'P19', 'P18', 'P17', 'P16', 'P15', 'P14', 'P13', 'P12', 'P11', 'P10', \
            'P09', 'P08', 'P07', 'P06', 'P05', 'P04', 'P03', 'P02', 'P01'    ]
    df = pd.read_excel(nomefile, header = None, names = colonne, sheet_name = 0)
    df_long  = pd.wide_to_long(df, stubnames=['P'], i = ['Area Manager', 'Manager', 'Prodotto'], j = 'Time')
    last_of_pred_month = date.today().replace(day=1) #- timedelta(days=1)
    obs = [last_of_pred_month - relativedelta(months= x[3]) for x in df_long.index]

    df_long['obs'] = obs
    print(df_long)    
    return df

def leggiMappa(nomefile):
    colonne = ['Referenza', 'Nome prodotto', 'Brand' ]
    df = pd.read_excel(nomefile, header = None, names = colonne, sheet_name = 1)
    return df 



# pulitura dati: (trim, replace spazi e _, fill (o drop) na)
# determinazione della percentuale di missing values
def stripColonna(dati, colonna):
    dati[colonna] = dati[colonna].str.strip()


def removeCharsColonna(dati, colonna, toRemove):
    for c in toRemove:
        dati[colonna] = dati[colonna].str.replace(c, '') 

def pulisciDati(dati):
    #trim
    daPulire = dati.select_dtypes(include='object').columns
    carDaEliminare = '_ '
    for col in daPulire:
        stripColonna(dati, col)
        removeCharsColonna(dati, col, carDaEliminare)

    daFillare = dati.select_dtypes(exclude=['object', 'category'])
    cna = daFillare.isna().sum().sum()
    dati.fillna(axis = 0, value = daFillare.mean(axis=0), inplace = True)

    return (cna / dati.select_dtypes(exclude=['object', 'category']).size)

# creare aggregati di colonne (somme) 12 a 12
def aggiungiColonneAnni(dati):
    dati['A1'] = dati.loc[:,'P24':'P13'].sum(axis = 1)
    dati['A0'] = dati.loc[:,'P12':'P01'].sum(axis = 1)

# calcolare le quote
# calcolare KPI

# trasporre il dato
# generare una serie di tipo temporale

# esportare
nomefile = 'esempio flusso dati.xlsx'
dati = leggiDati(nomefile)
mappa = leggiMappa(nomefile)

ratio = pulisciDati(dati)
print(f'dati puliti con ratio {ratio}')
aggiungiColonneAnni(dati)



dati.T.to_csv('puliti.csv')
#print(dati)