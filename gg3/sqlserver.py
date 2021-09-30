import pyodbc as sqls
import pandas as pd

conn = sqls.connect('DRIVER={SQL Server Native Client 11.0};SERVER=127.0.0.1;DATABASE=AdventureWorks;UID=sa;PWD=passw0rd;')

cursor = conn.cursor()
rows = cursor.execute('select * from Person.AddressType').fetchall()

records = pd.DataFrame((tuple(t) for t in rows))
'''
for row in cursor:
    records += (row)
    #print(row.Name)
'''
print(records)

products = pd.read_sql('select * from Production.Product', conn)
products.loc[products['MakeFlag']].to_excel('products.xlsx', sheet_name='Prodotti', index = None)

